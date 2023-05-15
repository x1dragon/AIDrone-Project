import pywifi
import time
from pywifi import const

try:
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    name = iface.name()
    iface.scan()


    x = time.sleep(5)



    networks = iface.scan_results()
    for data in networks:
        print("SSID:", data.ssid)
        print("BSSID:", data.bssid)
        print("Signal:", data.signal)
    
        try :
            print("Encryption:", str(data.encryption))
        except AttributeError:
            print("cant print the encrypytion type")


        if iface.status() in [const.IFACE_DISCONNECTED,const.IFACE_INACTIVE]:
            print("network card disconnected")

        else:
            print ("Network card connected")

except:
    print("An error occcured in the above code\n")

    print("ERROr: the  code failed to execute\nTroubleshoot ~ type 'iwconfig in the terminal and see if wlan0 is a module....' ")

