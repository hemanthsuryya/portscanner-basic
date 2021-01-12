#!/usr/bin/python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("[*] Enter host IP: ")
PORT = input("[*] Enter port: ")
PORT = int(PORT)
# PORT = 443

def portscanner(PORT):
    print("PORT     STATE")
    res = sock.connect_ex((HOST,PORT))
    if res:
        print(PORT,"     close")
    else:
        print(PORT,"     open")

portscanner(PORT)