# Impact of Network Partition Attacks on Blockchain Consensus

This repository contains a small-scale simulation study for investigating the effect of network partition attacks on blockchain consensus stability.

The project consists of:

- A discrete-time simulator modeling block propagation under network partitions.
- Experimental evaluation of fork rates, orphaned blocks, and reorganization behavior.
- A technical report describing the model, experiments, and results.

This is an academic simulation project, not intended to be a production blockchain implementation.

> [!NOTE]
> I will be using the 3-pass approach for going over the papers \
> Cite: [How to Read a Paper by S. Keshav](keshav@uwaterloo.ca)

> **Day 1**:
> - Scaffold simulation study
> - Setup latex
> - Select Papers for review

> **Day 2**: Literature Review
> - Majority is vulnerable: Nakamoto consensus is inherently not safe? by *Eyal and Sirer*
> - Information Propagation in Bitcoin by *Decker and Roger*
> - Blockchain protocols in async networks by *Shelat, Seeman*

> **Day 3**: Analysis of Day 2
> - Paper 1: Majority is not enough; Blockchain is vulnerable by *Eyat and Sirer* \
> [Notes](NOTES_P1.md)