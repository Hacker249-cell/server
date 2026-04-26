import socket

s = socket.socket()
s.bind(('127.0.0.1', 12345))
s.listen(1)

print("Waiting for connection...")
conn, addr = s.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()
    print("Client:", data)

    if data.lower() == "exit":
        break

    msg = input("Server: ")
    conn.send(msg.encode())

    if msg.lower() == "exit":
        break

conn.close()
s.close()