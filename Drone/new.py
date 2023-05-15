import nmap

# create a PortScanner object
scanner = nmap.PortScanner()

# specify the IP address range to scan
ip_range = '192.168.43.171/24'

# run the scan
scanner.scan(hosts=ip_range, arguments='-sS')

# iterate through the results
for host in scanner.all_hosts():
    print('Host:', host)
    print('State:', scanner[host].state())
    for proto in scanner[host].all_protocols():
        print('Protocol:', proto)
        for port in scanner[host][proto]:
            print('Port:', port, 'State:', scanner[host][proto][port]['state'])






