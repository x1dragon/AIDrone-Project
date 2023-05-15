import pywifi
from pywifi import const


class WifiScanner:
    def __init__(self):
        self.opened = []
        self.closed = []

    def scan_wifi(self):
        wifi = pywifi.PyWiFi()  # initialize pywifi
        iface = wifi.interfaces()[0]  # get the first wireless interface

        iface.scan()  # start scanning for wifi networks
        results = iface.scan_results()

        for result in results:
            if result.akm[0] == const.AKM_TYPE_NONE:  # check if the network is open
                self.opened.append(result.ssid)
            else:
                self.closed.append(result.ssid)

    def save_to_file(self):
        with open('opened.txt', 'w') as f:
            f.write('\n'.join(self.opened))
        with open('closed.txt', 'w') as f:
            f.write('\n'.join(self.closed))


if __name__ == '__main__':
    scanner = WifiScanner()
    scanner.scan_wifi()
    scanner.save_to_file()
