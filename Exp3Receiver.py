import socket
import struct

group = "224.1.1.1"
port = 5007

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", port))

mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print("Receiver started")

while True:
    data, addr = s.recvfrom(1024)
    print("From", addr, ":", data.decode())