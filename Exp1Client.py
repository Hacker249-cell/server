import socket

c = socket.socket()
c.connect(('127.0.0.1', 12345))

print("Connected to server")

while True:
    msg = input("Client: ")
    c.send(msg.encode())

    if msg.lower() == "exit":
        break

    data = c.recv(1024).decode()
    print("Server:", data)

    if data.lower() == "exit":
        break

c.close()