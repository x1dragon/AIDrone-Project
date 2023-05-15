import subprocess

#what this class does is that it checks to see if the adaptor is in monitor mode or not
#it does this by using "iwconfif and then relaying the out but to a file called "lol"
#this lol has the output of iwconfug which is later the interated through to see if it contains
#"monitor mode" ir somtheing else 


#remember this code will have to be changed when in corporated on the raspberry
#since the raspberry pi has  different hardware drivers so may not entireky be under the same drivers

class Adaptor_stat:#the name of the ckass
    
    def __init__(self):
        self.status = None
        
    def check_mode(self):
        # Run iwconfig and save output to file
        with open("lol", "w") as f:
            subprocess.run(["iwconfig"], stdout=f)

        # Read file and check if mode is Managed
        with open("lol", "r") as f:
            next_line = False
            for line in f:
                if "wlan0" in line:
                    next_line = True
                elif next_line and "Mode:Managed" in line:
                    with open("stat", "w") as f:
                        f.write("Managed")
                    self.status = "managed"
                    break
                else:
                    with open("stat", "w") as f:
                        f.write("Monitor")
                    self.status = "monitor"
                    next_line = False

            else:
                with open("stat", "w") as f:
                    f.write("Monitor")
                self.status = "monitor"


#remeber to check out the instanciation of the class
if __name__ == "__main__":
    adaptor = Adaptor_stat()
    adaptor.check_mode()
    print(f"The adapter is in {adaptor.status} mode")




#this class checks to see wether  the WIfi adaptor is in managed 
#or in monitor mode the code can work hand in hand with the network class
#to detwrmine if the Drone is in monitor mode