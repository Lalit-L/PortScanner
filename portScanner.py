import pyfiglet
import sys
import socket
from datetime import datetime
"""  
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
  
# Defining a target
if len(sys.argv) == 2:
     
    # translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of Argument")
"""

target = "127.0.0.1"
# Add Banner 
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)
