#!python3

from __future__ import print_function
from __future__ import unicode_literals

import socket
from dcsbios import ProtocolParser, StringBuffer, IntegerBuffer
import time

Debug = True

def load_json():
        import json
        f = open('F-16C_50.json')
        data = json.load(f)
        f.close()
        return data

Data = load_json()
parser = ProtocolParser()
Parsers = {}
Include = ["MASTER_ARM_SW", "RF_SW", "LASER_ARM_SW"]
for category in Data:
        for control in Data[category]:
                if(control in Include):
                        outputs = None
                        address = None
                        offset = None
                        mask = None
                        for item in Data[category][control]:
                                if str(item) == "outputs":
                                        outputs = item
                        if not outputs == None:
                                for item in Data[category][control][outputs][0]:
                                        if str(item) == "address":
                                                address = item
                                        if str(item) == "mask":
                                                mask = item
                                        if str(item) == "shift_by":
                                                offset = item
                                if not (address == None or mask == None or offset == None):
                                        control_Name = control
                                        control_address = Data[category][control][outputs][0][address]
                                        control_mask = Data[category][control][outputs][0][mask]
                                        control_offset = Data[category][control][outputs][0][offset]
                                        
                                        if Debug:
                                                print (category + ", " + control + ": [Address: " + str(control_address) + ", Mask: " + str(control_mask) + ", Offset: " + str(control_offset) + "]")
                                        Parsers[control_Name] = (IntegerBuffer(parser, control_address, control_mask, control_offset, lambda a, i=control_Name: print( i + ": ", a)))

if Debug:
        for item in Parsers:
                print(item + ": " + str(Parsers[item]))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7778))

print("Starting the scan loop:");

while 1:
	c = s.recv(1)
	parser.processByte(c)
