import socket

s = socket.socket()
s.bind(("127.0.0.1", 12345))
s.listen(1)

conn, addr = s.accept()
print("Connected")

while True:
    msg = conn.recv(1024).decode()
    print("Client:", msg)

    if msg == "exit":
        break

    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()
s.close()