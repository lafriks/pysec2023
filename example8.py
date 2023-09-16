"""Read and parse log file example"""

from datetime import timezone
import sys
from logutil.docker import Local

search = []
if len(sys.argv) > 1:
    search = sys.argv[1:]

# Parse docker container binary log format used by local driver
# docker run --rm --log-driver=local -p 8080:80 nginx
with open("testdata/container.log", "rb") as file:
    log = Local(file)

    for entry in log:
        has_match = len(search) == 0
        for f in search:
            if entry.message.find(f) >= 0:
                has_match = True
                break
        if has_match:
            time_local = entry.time.replace(tzinfo=timezone.utc).astimezone(tz=None)
            print(f"{time_local} [{entry.source}] {entry.message}")
