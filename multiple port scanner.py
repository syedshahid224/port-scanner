#!/usr/bin/python3
#Made by fireheart
import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)
host =  input(" Enter the Host to scan: ")
#port = int( input(" Enter the port to scan: "))
def portscanner(port):
        if sock.connect_ex((host, port)):
            print (colored("port %d is closed" %(port), 'red'))
        else:
            print (colored("port %d is open" %(port), 'green'))
#portscanner(port)
for port in range(1,1000):
    portscanner(port)
        


