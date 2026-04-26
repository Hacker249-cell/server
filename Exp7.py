# Simple Wait-For Graph
graph = {
    "P1": ["P2"],
    "P2": ["P3"],
    "P3": ["P1"],  # creates deadlock (cycle)
    "P4": ["P2"]
}

visited = set()
stack = set()

def dfs(node):
    visited.add(node)
    stack.add(node)

    for n in graph[node]:
        if n not in visited:
            if dfs(n):
                return True
        elif n in stack:
            return True

    stack.remove(node)
    return False


# Check deadlock
deadlock = False
for p in graph:
    if p not in visited:
        if dfs(p):
            deadlock = True
            break

print("Graph:")
for p in graph:
    print(p, "→", graph[p])

if deadlock:
    print("\nDeadlock Detected!")
else:
    print("\nNo Deadlock")