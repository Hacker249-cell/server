import socket, time

c = socket.socket()

T0 = time.time()
c.connect(("127.0.0.1", 5000))
c.send(b"time")

Ts = float(c.recv(1024).decode())
T1 = time.time()

c.close()

RTT = T1 - T0
sync_time = Ts + RTT/2

print("Server Time:", Ts)
print("RTT:", RTT)
print("Synchronized Time:", sync_time)