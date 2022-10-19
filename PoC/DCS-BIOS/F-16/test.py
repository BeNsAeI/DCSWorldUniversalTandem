#!python3

from __future__ import print_function
from __future__ import unicode_literals

import socket
from dcsbios import ProtocolParser, StringBuffer, IntegerBuffer

parser = ProtocolParser()

# address = 0x1000, length = 19
#cmspLine1 = StringBuffer(parser, 0x1000, 19, lambda s: print("CMSP LINE 1:", s))

# address = 0x1014, length = 19
#cmspLine2 = StringBuffer(parser, 0x1014, 19, lambda s: print("CMSP LINE 2:", s))

# address = 0x10e4, mask = 0x3800, shift_by = 11
cmspMode = IntegerBuffer(parser, 0x10e4, 0x3800, 11, lambda i: print("A-10 C II CMSP MODE: ", i))

# address = 0x10E8, mask = 0x000C, shift_by = 2
cmspMode = IntegerBuffer(parser, 0x10E8, 0x000C, 2, lambda i: print("A-10 C II MASTER ARM: ", i))

# address = 0x4424, mask = 0x0060, shift_by = 5
cmspMode = IntegerBuffer(parser, 0x4424, 0x0060, 5, lambda i: print("F-16 C MASTER ARM: ", i))

# uncomment to print all writes
# parser.write_callbacks.add(lambda address, data: print(address, data))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7778))

while 1:
	c = s.recv(1)
	parser.processByte(c)
