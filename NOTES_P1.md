## Majority is not Enough, Bitcoin mining is vulnerable by Eyal and Sirer

> **Assertion**: "Conventional wisdom asserts that the mining protocol is incentive-
compatible and secure against colluding minority groups, that is, it in-
centivizes miners to follow the protocol as prescribed."
> **Argument**: Bitcoin mining protocol is not incentive-compatible.
> - How: Selfish Mining

### Selfish Mining
Miners obtain unfairly larger revenue compared to honest miners.
- **Causes** honest miners to join the selfish miners, increasing the minorty colluding group's size until it becomes a majority
- **Results** in the network becoming centralized which defeats the purpose of distributed decentralization.

#### Feasibility

> [!NOTE]
> **How feasible is selfish mining?** \
> "Unless certain assumptions are made, selﬁsh mining may be feasible for
any group size of colluding miners."

### Modification proposed by the paper

Paper proposes a "practical" modification to the Bitcoin network that would protect the network generally.

**Proposal**: Prohibit selfish mining by groups that command leaa than 1/4 of the resource.

> [!IMPORTANT]
> **Reality**: Reliable discovery of selfish mining is hard at small scale. Even now, there is no protocol-level ban for such miners. \
> Faster block propagation, mining-pool policies, socio-economic pressure etc. have resulted in no large-scale documented selfish mining.

Unlike the theoretical, 51% limit, paper proposes much lower 25% limit, which they came at after certain assumptions.

### Statistics

1. Bitcoin has **12B