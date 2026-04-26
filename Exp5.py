import time

# Processes (1 to 5)
processes = {1: True, 2: True, 3: True, 4: True, 5: True}

coordinator = 5  # highest process initially

def show():
    print("\nProcesses:")
    for p in processes:
        print("P", p, "Alive" if processes[p] else "Down")
    print("Coordinator: P", coordinator)

def election(start):
    global coordinator
    print("\nElection started by P", start)

    higher = [p for p in processes if p > start and processes[p]]

    if not higher:
        coordinator = start
        print("New Coordinator: P", start)
        return

    for p in higher:
        print("P", start, "→", p)

    time.sleep(1)
    election(max(higher))


def crash(pid):
    global coordinator
    processes[pid] = False
    print("\nP", pid, "crashed")

    if pid == coordinator:
        print("Coordinator crashed!")
        alive = [p for p in processes if processes[p]]
        election(max(alive))


def recover(pid):
    processes[pid] = True
    print("\nP", pid, "recovered")
    election(pid)


# ---- Run ----
show()

crash(5)
time.sleep(1)
show()

recover(5)
time.sleep(1)
show()