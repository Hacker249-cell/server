import socket, time

s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen(1)

print("Server running...")

while True:
    conn, addr = s.accept()
    conn.recv(1024)   # receive request
    conn.send(str(time.time()).encode())  # send server time
    conn.close()