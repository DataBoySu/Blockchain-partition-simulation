import heapq
import random

# =============================
# Event system
# =============================

class Event:
    def __init__(self, time, action):
        self.time = time
        self.action = action

    def __lt__(self, other):
        return self.time < other.time


class Simulator:
    def __init__(self):
        self.time = 0.0
        self.event_queue = []

    def schedule(self, delay, action):
        event_time = self.time + delay
        heapq.heappush(self.event_queue, Event(event_time, action))

    def run(self, until):
        while self.event_queue and self.time <= until:
            event = heapq.heappop(self.event_queue)
            self.time = event.time
            event.action()


# =============================
# Blockchain data
# =============================

class Block:
    def __init__(self, height, parent_id, miner, timestamp):
        self.height = height
        self.parent_id = parent_id
        self.miner = miner
        self.timestamp = timestamp
        self.id = f"{height}-{miner}-{timestamp:.4f}"


# =============================
# Node
# =============================

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.chain = []

    def tip(self):
        return self.chain[-1]


# =============================
# MAIN SIMULATION
# =============================

if __name__ == "__main__":
    sim = Simulator()

    # ---- Genesis block ----
    genesis = Block(
        height=0,
        parent_id=None,
        miner="genesis",
        timestamp=0.0
    )

    # ---- Create nodes ----
    nodes = [Node(i) for i in range(3)]
    for n in nodes:
        n.chain.append(genesis)

    # ---- Mining logic ----
    BLOCK_RATE = 1.0  # blocks per unit time

    def mine_block(node):
        parent = node.tip()

        block = Block(
            height=parent.height + 1,
            parent_id=parent.id,
            miner=node.id,
            timestamp=sim.time
        )

        node.chain.append(block)
        print(f"[{sim.time:.2f}] Node {node.id} mined block {block.id}")

        # schedule next block for this node
        delay = random.expovariate(BLOCK_RATE)
        sim.schedule(delay, lambda: mine_block(node))

    # ---- Start mining ----
    first_delay = random.expovariate(BLOCK_RATE)
    sim.schedule(first_delay, lambda: mine_block(nodes[0]))

    sim.run(until=10.0)
