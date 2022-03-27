import socket
from IPy import IP
from modules import ip

def main():
    text = ip.get_ip()
    print(text)

if __name__ == "__main__":
    main()