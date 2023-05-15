import scapy
import socket
import fcntl
import struct
import smtplib
import os



def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15].encode()))[20:24])

def get_gateway(ifname):
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[0] == ifname:
                return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
    return None

def get_subnet_mask(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x891b, struct.pack('256s', ifname[:15].encode()))[20:24])
        return ip
    

ifname = "wlan0"

gateway = get_gateway(ifname)
IP = get_ip_address(ifname)
Subnet = get_subnet_mask(ifname)


total = [gateway, IP , Subnet]


try:
    response = os.system("ping " + gateway + " -c 1")
    if response == 0:
        print("Gateway is Active ")


except OSError:
    print("code didnt execute right")
    
else:
    print("Gateway is : " + gateway  )
    print("Subnet is : "+ Subnet) 





#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#hostname = socket.gethostname()
#port  = 666

#host = 'www.google.com'
#portg = 80

#try:
#    s.connect(host, portg)

#    request = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"

#    s.send(request.encode )
#    respons =  s.recv(1024)

#    print(respons.decode)
#    s.close()
#except TypeError:
#    print("Couldnt connect to remote server ")







    
 













