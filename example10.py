"""Example on using threads"""

from datetime import timezone
import sys
from threading import Lock, Thread
from logutil.docker import Local, LogEntry

log_entries = list()
log_entry_lock = Lock()

def add_log_entry(entry: LogEntry):
    """Threadsafe function to add logs to central list"""

    with log_entry_lock:
        log_entries.append(entry)

def filter_log(path: str, search: list[str]):
    """Filter log file"""

    with open(path, "rb") as file:
        for entry in Local(file):
            has_match = len(search) == 0
            for f in search:
                if entry.message.find(f) >= 0:
                    has_match = True
                    break
            if has_match:
                entry.time = entry.time.replace(tzinfo=timezone.utc).astimezone(tz=None)
                add_log_entry(entry)

# python example10.py testdata/container.log testdata/container2.log GET
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("example10 <log-files> <search[,search]>")
        sys.exit(1)

    # Start thread for each log file
    threads = list()
    for log in sys.argv[1:-1]:
        args = [log]
        args.append(str(sys.argv[-1]).split(','))
        t = Thread(target=filter_log, args=args)
        threads.append(t)
        t.start()

    # Wait for all threads to finish searching log files
    for t in threads:
        t.join()

    if len(log_entries) == 0:
        print("no log records found")
        sys.exit(127)

    # Print sorted entries
    for e in sorted(log_entries, key=lambda e: e.time):
        print(f"{e.time} [{e.source}] {e.message}")
