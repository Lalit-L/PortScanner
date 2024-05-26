import pyfiglet
import sys
import socket
from datetime import datetime

# Banner
ascii_banner = pyfiglet.figlet_format("TOTAL PORT SCANNER V. 1")
print(ascii_banner)

# Local Host to make sure it's not used in an illegal manner
target = "127.0.0.1"
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

# Tries to connect to each port
try:
     
    for port in range(1,20000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
         
# Exceptions/interruptions that stop the program
except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

