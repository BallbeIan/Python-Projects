import os
import socket
import argparse

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
    parser = argparse.ArgumentParser(description="Collects the IP/DNS and ports of" \
    "the target to scan."
    )
    parser.add_argument("--t", required=True, type=str)
    parser.add_argument("--p", required=True, type=int)
    args=parser.parse_args()

    target = args.t
    port = args.p

    scan(target,port)