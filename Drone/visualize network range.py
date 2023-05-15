import matplotlib.pyplot as plt
import pywifi
import time

class signalvizualization:
    
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]
    
    def scan(self):
        self.iface.scan()
        time.sleep(8)
        results = self.iface.scan_results()
        x = [b.ssid for b in results]
        y = [b.signal for b in results]
        plt.bar(x, y)
        plt.xlabel("Wi-Fi Networks")
        plt.ylabel("Signal Strength (dBm)")
        plt.title("Closest Wi-Fi Networks")
        plt.xticks(rotation=90)
        plt.show()

# Example usage:
vizualizer = signalvizualization()
vizualizer.scan()

