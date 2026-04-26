import socket

c = socket.socket()
c.connect(("127.0.0.1", 12345))

print("Connected")

while True:
    msg = input("Client: ")
    c.send(msg.encode())

    if msg == "exit":
        break

    reply = c.recv(1024).decode()
    print("Server:", reply)

c.close()