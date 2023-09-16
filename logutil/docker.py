"""Docker file format reader"""

from datetime import datetime
from io import BufferedReader
import struct
from protobuf_decoder.protobuf_decoder import Parser

ENCODE_BINARY_LEN = 4

class LogEntry:
    """Log entry"""

    def __init__(self, source: str, time_ns: int, message: str):
        self.source = source
        self.time = datetime.utcfromtimestamp(time_ns / 1e9)
        self.message = message

class Local:
    """Docker local driver log file reader"""

    def __init__(self, file: BufferedReader):
        self.file = file
        self.offset = 0
        self.next_msg_len = 0
        self.buf = bytes()

    def __iter__(self):
        return self

    def __next__(self) -> LogEntry:
        try:
            rec = self.__read_record(ENCODE_BINARY_LEN)
            if not rec:
                raise StopIteration
            msglen, = struct.unpack(">I", rec)
            rec = self.__read_record(msglen+ENCODE_BINARY_LEN)
            if not rec:
                raise StopIteration

            parsed = Parser().parse(rec[0:len(rec)-ENCODE_BINARY_LEN].hex())

            return LogEntry(
                str(parsed.results[0].data),
                int(parsed.results[1].data),
                str(parsed.results[2].data))
        except StopIteration:
            raise
        except Exception as ex:
            raise StopIteration from ex
        

    def __read_record(self, size: int) -> bytes:
        buf = self.file.read(size)
        if len(buf) < size:
            raise EOFError()

        return buf
