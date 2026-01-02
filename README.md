# Blockchain Network Partition Simulation —> Plan of Action

1. This repository shall contain a small-scale, abstract simulation for studying network partition attacks against longest-chain proof-of-work blockchains.

2. The repository documents the scope of the model, the metrics I will collect, the single-file code design, and the structure of a 5–6 page writeup.

No networking, no async, and no message-level simulation — this is an abstract, discrete-time model intended for reproducible experiments and metrics collection.

**3. Scope**

- **Single deliverable:** a concise simulation and a 5–6 page writeup. No additional features will be added beyond what I have specified here.
- **Academic framing:** a small-scale simulation (N on the order of tens), intended to support my experimental claims about partition-induced divergence and recovery.

**3.1 Model**

- **Nodes:** N nodes (example: N = 50). Each node represents a miner capable of producing blocks.
- **Topology:** random graph connectivity (undirected). Connectivity is represented as an adjacency matrix/list; edges determine which nodes are in the same connected component.
- **Mining:** each node follows a Poisson mining process (discrete-time approximation: each tick a node mines with probability derived from its Poisson rate).
- **Consensus rule:** longest-chain rule; nodes adopt the longest chain they are aware of at each tick.
- **Time:** discrete ticks. The simulation advances in uniform steps; blocks are produced and chain updates are applied at tick boundaries.
- **Partition event:** at time T_p, the network is split into two components (by dropping all cross-component edges). Nodes inside each component continue mining independently.
- **Reconnection:** at time T_r > T_p, cross edges are restored and nodes exchange chain information (abstracted: nodes compare chain lengths and adopt the longest chain).

Notes: this model is intentionally abstract. There are no low-level messages, propagation delays, or asynchronous queues — only the connectivity graph and per-tick state updates.

**3.2 Metrics**
We record the following metrics:

- **Fork depth:** maximum depth at which branches diverge between the two components during the partition.
- **Number of orphaned blocks:** total count of blocks that are ultimately not in the converged longest chain after reconnection.
- **Time to convergence:** number of ticks from reconnection until the network reaches a single common longest chain (or a defined convergence threshold).
- **Max divergence between components:** maximum difference in chain length (or best-chain cumulative work) observed between the two components during the partition.

Each metric will be logged per-run and suitable for CSV export and basic plotting (histogram/time-series/boxplots) to support my experimental claims.

**3.3 Code**

- **Single Python script:** a single script (e.g., `simulate.py`) will contain the model and runner.

Responsibilities:

- Define `Node` and `Network` abstractions (lightweight, deterministic state machines).
- Implement the discrete-time tick loop, Poisson mining per node, chain updates under the longest-chain rule, partition and reconnection events.
- To Collect and log the metrics I listed above.
- Output results as CSV and optionally emit simple Matplotlib plots.

- **Implementation constraints:**
- No real networking, no message-level simulation, no async/threads.
- Deterministic random seeds for reproducibility.
- Configurable parameters: `N`, graph density, per-node mining rate, `T_p`, `T_r`, number of runs.

This abstract approach is for understanding plus a write-up, as a small-scale simulation for exploring partition dynamics and measuring high-level effects on chain divergence and recovery.

**4 Writeup Structure (5–6 pages)**

- **Introduction:** concise problem statement, goals, and high-level contributions.
- **Background:** brief background on longest-chain consensus, partition attacks, and why small-scale simulations can be informative.
- **Model:** describe the node/network model, discrete-time ticks, Poisson mining approximation, partition/reconnect procedure, and the metrics collected (no heavy proofs).
- **Experiment:** experimental setup, parameter choices, number of runs, and how results are aggregated.
- **Results:** plots and tables showing fork depth, orphaned blocks, convergence times, and divergence statistics; concise interpretation.
- **Discussion & Limitations:** limitations of the abstract model (no message-level propagation, simplified topology), implications for larger networks, and directions for future work.

> [!NOTE]
> References: 2–3 key references.

---
