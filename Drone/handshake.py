from scapy.all import *

#interface = "wlan0"  # replace with the name of your wireless interface
#ssid = "my_wifi_network"  # replace with the name of the target wireless network
#handshake_count = 0

#def capture_handshake(pkt):
#    global handshake_count
#    if pkt.haslayer(EAPOL) and pkt.haslayer(Dot11):
#        if pkt[Dot11].addr1.lower() == "ff:ff:ff:ff:ff:ff" or pkt[Dot11].addr2.lower() == "ff:ff:ff:ff:ff:ff":
#            if pkt[Dot11].info.decode('utf-8') == ssid:
#                if pkt[EAPOL].type == 3:
#                    handshake_count += 1
#                    wrpcap(f"{ssid}_{handshake_count}.cap", pkt, append=True)

#print(f"Capturing WPA2 handshakes for {ssid}...")

#sniff(iface=interface, prn=capture_handshake)