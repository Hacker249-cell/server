import socket

group = "224.1.1.1"
port = 5007

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

print("Sender started")

while True:
    msg = input("Send: ")
    
    if msg == "exit":
        break
    
    s.sendto(msg.encode(), (group, port))

s.close()