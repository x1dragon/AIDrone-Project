#!/usr/bin/python
#final 
#this code is property of x1ryu  ahengjnr@gmail.com
#remember to turn this sample code into a function and add it to the "/programming/Drone/networkclass.py" file in the future

import scapy, os, re, nmap
import socket
import struct
from networkclass import *
import time



#ifname = 'wlan0'
Network.get_gateway()

#this was an older implementation of the code below
#function to get the gateway of the network interface 
#def get_gateway(ifname):
#    with open("/proc/net/route") as fh:
#        for line in fh:
#            fields = line.strip().split()
#            if fields[0] == ifname:
#                return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
#    return None

#we call and store the value of the gateway ivariable gateway




#gateway =  get_gateway(ifname)

#importing the gateway from networkclass.py
#after remember to turn this scanning feature into a class
gateway = Network.get_gateway()



print(f"perfoming default port scan 70 - 80 .... on {gateway}")


#making script sleep for some seconds

time.sleep(2)



#begin = int(input("input a number"))
#end = int(input('input a number'))

begin = 70
end = 80 

target = str(gateway)

scanner = nmap.PortScanner()

for i in range(begin, end+1):
    res = scanner.scan(target, str(i))
    #print(res)
    state = res['scan'][target]['tcp'][i]['state']
    print(f'port {i} is {state} on {target}')








