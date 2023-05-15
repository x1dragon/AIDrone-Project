import os
import re
import time

class Arpscan:
    def __init__(self, interface):
        self.interface = interface

    def get_ip_address(self):
        ip_output = os.popen('ip addr show ' + self.interface).read()
        match = re.search(r'inet ([\d.]+)', ip_output)
        if match:
            return match.group(1)
        
        else:
            return None

    def scan_network(self, output_file=None):
        ip_address = self.get_ip_address()
        if ip_address:
            command = f'arp-scan --localnet --interface={self.interface}'
            output = os.popen(command).read()
            lines = output.splitlines()[2:-4]
            devices = []
            if output_file:
                with open(output_file, "w") as f:
                    for line in lines:
                        fields = line.split()
                        devices.append({'ip':fields[0], 'mac':fields[1]})
                        f.write(fields[0]+'\n')
            else:
                for line in lines:
                    fields = line.split()
                    devices.append({'ip':fields[0], 'mac':fields[1]})
            return devices
        else:
            return None


scanner = Arpscan('wlan0')
devices = scanner.scan_network(output_file='network devices.txt')
if devices:
    print(f'Found {len(devices)} devices on the network:')
    for device in devices:
        print(f'{device["ip"]} ({device["mac"]})')
else:
    print('Unable to determine network interface information or no devices on the network.')