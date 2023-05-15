import nmap
import time
from networkclass import *


class NetworkScanner:
    def __init__(self):
        self.gateway = Network.get_gateway()

    def vuln(self):
        portss = [80, 443, 23, 22, 7547]
        scanner = nmap.PortScanner()

        print("scanning for most likeley vulnerable services or ports\n\n")

        with open(str(self.gateway), "w") as i:
            i.write(
                f"Scaning for common services on target {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            for port in portss:
                port_str = str(port)

                res = scanner.scan(self.gateway, port_str,
                                   "-vv -sS -sV -sC -A -O")
                print(scanner.scaninfo())
                state = res['scan'][self.gateway]['tcp'][port]['state']
                i.write(f"Port {port_str}: {state}\n")
                print(f"Port {port_str} is {state} on {self.gateway}")

            if port == 80 and state == "open":
                print("likely hosting a web service...\n\n")
                print("testing for  DOS vulnerabilities")

            elif port == 443 and state == 'open':
                print('service tunning on port 443')
                # add a more defined function to this

            elif port == 23 and state == 'open':
                print('port is like likely running telnet')

            elif port == 22 and state == 'open':
                print('the gateway has port 22 enabled')

            elif port == 22 and state == "closed":
                print('there is no ssh enabled on this target')

            elif port == 80 and state == "closed":
                print("port 80 isnt vulnerable")

    

    #this code has bugged so many times 
    def activehosts(self):
        scanner = nmap.PortScanner()
        # using the get.cidr_note method form the network class script and assigning it to cidr
        cidr = str(Network.get_cidrnote())
        print(f"scanning hosts in {cidr}")
        results = scanner.scan(hosts=cidr, arguments='-sS')

        # iterate through the results
        for host in results['scan']:
            print('Host:', host)
            print('State:', results['scan'][host]['status']['state'])
            if 'tcp' in results['scan'][host]:
                for port in results['scan'][host]['tcp']:
                    if results['scan'][host]['tcp'][port]['state'] == 'open':
                        print('Protocol:', 'tcp', 'Port:', port, 'State:', results['scan'][host]['tcp'][port]['state'])


                    

#    def port_scan(self, begin, end):
#        try:
#            target = str(self.gateway)
#            scanner = nmap.PortScanner()
#        except:
#            print("erro no interface UP")
#
#        with open("scan_results.txt", "w") as f:
#            f.write(f"Scan started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
#            for i in range(begin, end+1):
#                res = scanner.scan(target, str(i))
#                state = res['scan'][target]['tcp'][i]['state']
#                f.write(f"Port {i}: {state}\n")
#                print(f"Port {i} is {state} on {target}")

#            f.write(f"Scan completed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
# network_scanner = NetworkScanner()
# network_scanner.port_scan(70, 80)
scan = NetworkScanner()
#scan.vuln()
scan.activehosts()
# scan.networksweep()
