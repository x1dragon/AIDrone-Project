import socket
import time
import os
import re
import fcntl
import struct
import requests
import nmap
import netifaces
import subprocess

# this code was written by Aheng jr, x1Ryu.corp


class Network:
    ifname = "wlan0"

    def __init__(self):
        self.ip = ''
        self.gateway = ''
        self.pub_ip = ''
        self.get_cidr = ''

    # this is to find the gate way adress from the /proc/net/route
    # could have used the os.systemmodule ("arp -a") but wouldve been a more complex move since id had had to splut the results into and array and print the value out in a tuple or smth
    def get_gateway(self):

        with open("/proc/net/route") as fh:
            for line in fh:
                fields = line.strip().split()
                if fields[0] == self.ifname:
                    return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

       # get local ip from memory storage from "0x8915"

    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', self.ifname[:15].encode()))[20:24])

    def get_public_ip(self):
        retries = 0
        max_retries = 10
        timeout = 30
        while retries < max_retries:
            try:
                ip_address = requests.get(
                    'https://api.ipify.org', timeout=timeout).text
                self.public_ip = ip_address
                return
            except (OSError, requests.exceptions.RequestException):
                retries += 1
                print("Trying to connect... ")
                time.sleep(2 ** retries)
        raise Exception("Unable to get public IP")

    def arpscan(self):
        pass
    

    def get_cidrnote(self):
        result = subprocess.run(['ip', 'a'], capture_output=True, text=True)
        lines = result.stdout.splitlines()

        wlan0_line = None
        for line in lines:
            if 'inet ' in line and 'wlan0' in line:
                wlan0_line = line
                break

        self.get_cidr = wlan0_line.split()[1]
      
       
        return self.get_cidr
 
#    def nmapnetworkscan(self):
#        subnetcidr = self.get_cidrnote()
        
        





    

#scan for devices using an ARP and saving it to a file
    
        









 #   def port_scan(self):


Network = Network()





#Network.nmapnetworkscan()
# while True:
#  try:
#    network.get_public_ip()
#    print("IP:", network.get_ip_address())
#    print("Gateway:", network.get_gateway())
#    print("Public IP:", network.public_ip)
#    break
#  except OSError:

#   def loading():
#    while True:
#        for i in range(4):
#            print("\r retrying connection" + "." * i, end="")
#            time.sleep(0.5)
