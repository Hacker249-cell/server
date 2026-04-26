import random

servers = [0, 0, 0]   # load of 3 servers
index = 0

# Round Robin
def round_robin(task):
    global index
    print("Task", task, "→ Server", index)
    servers[index] += 1
    index = (index + 1) % len(servers)

# Least Loaded
def least_loaded(task):
    s = servers.index(min(servers))
    print("Task", task, "→ Server", s)
    servers[s] += 1

# Random
def random_assign(task):
    s = random.randint(0, 2)
    print("Task", task, "→ Server", s)
    servers[s] += 1

def show():
    print("Load:", servers)


# ---- Run ----
tasks = range(1, 6)

print("\nRound Robin")
for t in tasks:
    round_robin(t)
show()

print("\nLeast Loaded")
for t in tasks:
    least_loaded(t)
show()

print("\nRandom")
for t in tasks:
    random_assign(t)
show()