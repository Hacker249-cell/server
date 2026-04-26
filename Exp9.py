import threading
import time

class DSM:
    def __init__(self, num_nodes):
        self.memory = {"x": 0}  # shared variable
        self.nodes = [Node(i, self) for i in range(num_nodes)]

    def broadcast_update(self, key, value, source_id):
        print(f"\n Broadcasting update: {key} = {value} from Node {source_id}")
        for node in self.nodes:
            if node.node_id != source_id:
                node.update_local_copy(key, value)

class Node:
    def __init__(self, node_id, dsm):
        self.node_id = node_id
        self.dsm = dsm
        self.local_memory = dict(dsm.memory)

    def read(self, key):
        value = self.local_memory.get(key, None)
        print(f"Node {self.node_id} READ {key} = {value}")
        return value

    def write(self, key, value):
        print(f"\n Node {self.node_id} WRITE {key} = {value}")
        self.local_memory[key] = value

        # Update global memory
        self.dsm.memory[key] = value

        # Broadcast change to other nodes
        self.dsm.broadcast_update(key, value, self.node_id)

    def update_local_copy(self, key, value):
        print(f"Node {self.node_id} updating {key} = {value}")
        self.local_memory[key] = value

# ---- Simulation ----
def node_work(node):
    time.sleep(node.node_id)

    node.read("x")
    new_value = node.node_id * 10
    node.write("x", new_value)
    time.sleep(1)
    node.read("x")

if __name__ == "__main__":
    dsm = DSM(3)

    threads = []
    for node in dsm.nodes:
        t = threading.Thread(target=node_work, args=(node,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
