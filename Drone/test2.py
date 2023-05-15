import os 



os.system("ifconfig > status")



try:
    while True:

        with open("/home/x1dragon/Documents/progamming/Drone/status", "r") as file: #open the  status file
            output = file.readlines()# the output of the file
            print(output)
            if "wlan0" in output:
                print("the drone is in managed Mode!")

            elif "wlan0mon" in output:
                print("The Drone is now in monitor mode!.....")
                break;
        
            else:
                print("type 'iwconfig' in terminal to check for wireless module\n")
                print("ERROR~:The adapter 'wlan0' doesnt seem to exist")


        
except:
    print("An error occured")


