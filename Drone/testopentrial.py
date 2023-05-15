import wifi

# Scan for available WiFi networks
cells = wifi.Cell.all('wlan0')

# Print information about each network
for cell in cells:
    print('SSID:', cell.ssid)
    print('Signal strength:', cell.signal)
    print('Encryption:', cell.encryption_type)
    print()




