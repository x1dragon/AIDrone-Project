import nmap
import time
from networkclass import *

class NetworkScanner:
    def __init__(self):
        self.gateway = Network.get_gateway()

    def port_scan(self, begin, end):
        try:
            target = str(self.gateway)
            scanner = nmap.PortScanner()
        except:
            print("errot no interface UP")

        with open("scan_results.txt", "w") as f:
            f.write(f"Scan started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            for i in range(begin, end+1):
                res = scanner.scan(target, str(i))
                state = res['scan'][target]['tcp'][i]['state']
                f.write(f"Port {i}: {state}\n")
                print(f"Port {i} is {state} on {target}")

            f.write(f"Scan completed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

network_scanner = NetworkScanner()
network_scanner.port_scan(70, 80)
