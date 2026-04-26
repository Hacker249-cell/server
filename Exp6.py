import threading
import time

# Shared variables
n = 3
clock = 0
request = [False]*n
reply_count = [0]*n

def request_cs(i):
    global clock
    clock += 1
    request[i] = True
    print(f"\nProcess {i} requesting CS")

    # Send request to others
    for j in range(n):
        if j != i:
            receive_request(i, j)

    # Wait for replies
    while reply_count[i] < n-1:
        time.sleep(0.1)

    # Enter CS
    print(f"Process {i} ENTER CS")
    time.sleep(1)
    print(f"Process {i} EXIT CS")

    request[i] = False
    reply_count[i] = 0


def receive_request(sender, receiver):
    # Always send reply (simplified logic)
    print(f"{receiver} → REPLY → {sender}")
    reply_count[sender] += 1


# Run threads
threads = []

for i in range(n):
    t = threading.Thread(target=request_cs, args=(i,))
    threads.append(t)

for t in threads:
    t.start()
    time.sleep(0.5)

for t in threads:
    t.join()