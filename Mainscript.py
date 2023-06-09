#!/bin/python3
#this code is property of aheng jr x1ryu.corp
# email:ahengjnr@gmail.com 
# Look for open wifi hotspots, connect, harvest ip
# Main issue: open spots are not efficiently found (bot grabs hidden too).
#             Future update: ensure only open are grabbed
from os import system as sys  # Allows me to control network manager
from os import geteuid as usertype  # Allows me to prevent non-root use
from sys import exit as terminate  # Allows me to generate exit codes
from sys import argv  # Allows me to read arguments
from termcolor import colored as color  # Allows me to make the terminal display colorful
from re import findall as find  # Allows me to use regular expressions
from urllib import request    # Allows me to send a web request to get the ip
from time import sleep  # Allows me to limit the speed, reducing CPU demand

# ============ Functions ============
connected = False 

def info(content, bad=False):
    '''
    This prints info to the terminal in a fancy way
    '''
    if not bad:
        print(color('[i] ', 'blue') + color(content, 'white'))
        
    else:
        print(color('[X] ', 'red') + color(content, 'white'))


def scan():  # Function 1
    '''
    This orders a scan of the environment and displays the results
    if no hotspots are located. This is the main function of the script.
    '''
    sys('sudo nmcli dev wifi rescan')  # Scan environment now
    sys('sudo nmcli dev wifi > hotspots')  # Send info over environment to file
    sys('sudo chmod 755 hotspots')  # Change this file's permissions
    with open('hotspots', 'r') as file:  # Open the new file in Python
        content = file.read()  # Save the file's content to spots
        sys('clear')  # Clears the terminal 
        print(color(content, 'white'))  # Prints wifi hotspots around you 
        
        # 1. Split file by newline
        content = content.split('\n')
        
        # 2. Determine if there's an open spot
        global connected

        for content in content:
            try:
                bssid = content.split(' ')[8]  # At [8] lies the BSSID
            
            except:  # Something is going wrong
                with open('blackbox', 'a') as blackbox:  # Open bug record file
                    blackbox.write(str(content.split(' ')) + '\n')  # Add the info for later review
                    continue
            
            
            if '--' in content and not inBlacklist(bssid):  # If the hotspot is open and not in the blacklist
                # 3. Connect to hotspot               
                if connect(bssid) and internetAccess():
                    ip = harvestIP()
                    if not ip == 'err':  # If the error code was not returned
                        saveInfo(ip) 
                        connected = True
                         # Write the info to the file
                        break
                        
                    else:  # If for some reason an error popped up
                        addToBlacklist(bssid)
                        continue
                else:
                   addToBlacklist(bssid)
                   continue
        
def connect(bssid):  # Function 2
    '''
    This connects to a hotspot
    
    :Param: string BSSID
    :Return: bool indicating status
    '''
    
    # 1. Connect to wifi hotspot
    info('Attempting to connect to hotspot')
    sys('sudo nmcli dev wifi rescan')
    sys('sudo nmcli dev wifi connect %s > status' % bssid)  # Connect to BSSID and output to file
    sys('sudo chmod 755 status')
    with open('status', 'r') as file:
        if 'successfully activated' in file.read():
            sys('sudo rm status')  # Delete temporary file
            info('Connected')
            return True  # True represents that the connection was successful
        else:
            sys('sudo rm status')
            info('Failed to connect', bad=True)
            return False  # False represents that the connection failed

def internetAccess():  # Function 3
    '''
    This function determines if the connection has internet by pinging
    Google's DNS
    
    :Return: bool representing the ability to access internet
    '''
    
    info('Testing internet access')
    sys('ping -c4 8.8.8.8 > pingInfo')  # Pinging Google's DNS server should work to identify access; does this 4x
    sys('sudo chmod 755 pingInfo')
    with open('pingInfo', 'r') as file:
        try:
            content = file.read().split('\n')[7].split(' ')[3]  # This gets the value associated with recieved responses
            if int(content) > 0:  # As long as one ICMP ping was recieved
                info('Internet access confirmed')
                return True  # True represents internet access
            else:
                info('No internet access', bad=True)
                return False
                
        except Exception as e:  # Something has gone wrong. Report failure
            info('Error: %s' % str(e))  # These failures dont tend to be an issue; may indicate authentication requirement
            return False
    

def inBlacklist(bssid):
    '''
    Determines if bssid is in blacklist
    
    :Param bssid: string BSSID
    :Return: bool representing membership; true if in, false otherwise
    '''
    try:
        with open('blacklist.txt', 'r') as file:  # Open blacklist file
            content = file.read()  # Get content of blacklist
            if bssid in content:  # If you can find the requested BSSID, it has been blacklisted
                return True  # True represents that it was found
            else:
                return False
    except:  # Likely cause is that the file does not exist as it hasn't been created yet 
        return False
        

def addToBlacklist(bssid):
    '''
    This function adds a bssid to the blacklist
    
    :Param: string bssid
    :Return: None
    '''
    with open('blacklist.txt', 'a') as file:  # Create or append to the blacklist
        file.write(bssid + '\n')  # Write the bad BSSID to blacklist file
        info('Added %s to blacklist' % bssid, bad=True)    
    
        
def harvestIP():  # Function 4
    '''
    This retrieves an IP address
    
    :Return: string ip
    '''
    
    info('Trying to get IP address')
    try:
        # The HTML variable is obtained by asking duckduckgo what's the ip and decoding the response
        html = request.urlopen('https://duckduckgo.com/?q=whats+my+ip&ia=answer').read().decode('utf-8')
        visIP = find('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', string=html)[0]  # Find IP in request HTTP response
        with open('bufferIP', 'a') as file:  # Potentially unnecessary premature saving of found data (will be removed later)
            file.write(str(visIP) + '\n') 
        return visIP  # Return IP
    
    except:
        info('Faild to acquire IP address', bad=True)
        return 'err'  # If err, the bot failed to get a correct response 
    
def saveInfo(ip):  # Function 5
    '''
    This saves the ip to the output list
    
    :Param ip: string ip address
    :Return: None
    '''
    try:
        with open('ips.txt', 'a') as file:  # This is the file that will contain the sweet sweet IP addresses
            file.write(ip + '\n')  # Wirte each address and a newline character 
            info('Saved IP address to file')
    
    except Exception as e:
        info('Error: %s' % str(e))  # This will help me debug if something goes wrong
        
# ============ START HUNT ============

try:  # Get sleep time argument if there
    wait = float(argv[1])  # This must be a numerical value 
except:
    wait = 3  # If no numercial value was inputted, default wait is three seconds


# 1. Determine user type, require root
if not usertype() == 0:  # If the user is not root
     info('Must run script as root', bad=True)  # Scold user
     terminate(1)  # Report failure

# 2. Start hunting loop
ct = 0
while not connected: # Keep looping until connected is set to True 
    scan()
    info('Current iteration: %s' % str(ct))
    info('Waiting for %s seconds ...' % str(wait))
    ct += 1
    sleep(wait)
    
terminate(0)  # CTRL+C to end. This is the normal way of exiting 