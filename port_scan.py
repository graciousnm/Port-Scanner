import threading
import socket
from colorama import Fore, Style
import os
import time

os.system('cls')
banner = Fore.RED+ r"""
                    ######################****************#######################
                     ____            _        ____                                  
                    |  _ \ ___  _ __| |_     / ___|  ___ __ _ _ __  _ __   ___ _ __ 
                    | |_) / _ \| '__| __|    \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
                    |  __/ (_) | |  | |_      ___) | (_| (_| | | | | | | |  __/ |   
                    |_|   \___/|_|   \__|    |____/ \___\__,_|_| |_|_| |_|\___|_| 

                                      Version:1.0 - By: @gracious
                                      https://github.com/graciousnm
                                      Use at your own risk

                    ######################****************#######################
"""
print(banner)

host = input("Enter the IP Address to Scan : "+ Fore.WHITE )
print("\n" + Fore.BLUE +"[+] "+ Fore.YELLOW + "Scanning Ports for host : " + Fore.WHITE + host + "\n")
time.sleep(3)



def scan_port(host, port):
    try:
        #creating a tcp socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server on local host and the given port number.
        #storing results in a variable
        s.settimeout(1)
        result = s.connect_ex((host, port))
        #getting the open ports printed to the terminal
        if result == 0:
            print(Fore.GREEN + "[+] " + Fore.WHITE + "Port {} is open".format(port) + Style.RESET_ALL)
            
        #closing connection after scanning for the open ports
        s.close()
        

    except socket.error as e:
        print("Caught an error while scanning port" + str(e))

#creating threads for each single port to be scanned
def thread_port(ports, host):
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)

        t.start()
        
    for t in threads:
        t.join()


ports = range(1, 63536)

#calling the thread function    
thread_port(ports, host)
