import os
import socket

def scan(target,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    result = s.connect_ex((target, int(port)))
    
    if result == 0:
        ip_address = socket.gethostbyname(target)
        print(f"Port {port} is open")
        print(f"IP: {ip_address}")
    else:
        print("Not found")

#============================================================================================================

if __name__ == "__main__":
    target = input("Who is the target? ")
    port = int(input("What port? "))
    scan(target,port)