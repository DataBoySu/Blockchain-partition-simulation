## Contextual Claims (Not Used in Simulator)

- Paper argues Bitcoin mining is not incentive-compatible.
- Paper discusses risks of centralization due to selfish mining.
- Bitcoin market cap (~$12B in Jan 2014) cited for motivation.
- FLOPS-equivalent comparisons used rhetorically.

Nonce: Random 32-bit number

Earlier miners used CPUs, around 2014, ASIC machines gained significance, these machines spealize in only one thing, performing SHA-256 Operations(for solving PoW puzzles) getting to magnitudes higher processing power than traditional CPU, which is generalist, and GPU which is specialized for Graphics and MM.

- ASIC: Application-Specific Integrated Circuit Machines

## Background Info

- Blockchain whitepaper published in 2008, by Satoshi Nakamoto.
- In Jan 2009, S.N. mined the first block, **the genesis block of Bitcoin** with message "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."; Launching the network
- First real transaction was S.N. sending 10 BTC to dev Hal Finney in 2009
- 2021 Shortages of GPUs is a result of Ethereum network's PoW(Ethash) which was GPU friendly unlike Bitcoin.
- In 2022, Ethereum switched to PoS, for efficiency and world peace.

> [!NOTE]
> Bitcoin -> ~10 minute block, slower and more expensive for small transactions \
> Ethereum -> ~12 second block

- Bitcoin has fixed supply of only 21M BTC, intention is to create more demand than supply.
- New Coins are created; but the rate is halved every 4 years. Started at 50BTC, now, 6.25BTC.
- Once BTC is completely mined out, no more. Miners will have to rely on transaction fees.

- Ethereum uses Solidity as its language, being Turing-complete, is like a general purpose computer.
- Bitcoin is just transactions, no if-else, nothing.
  
> [!IMPORTANT]
> Ethereum is programmable ledger, with VMs at every node \
> Bitcoin is like gold. Will mine the last coin in 2140.

- Colluding groups of miners are formed to decrease income variance, each member contributes and receives rewards based on their contribution. [Centralization]

## Surrounding Context
-  [Kroll, J.A., Davey, I.C., Felten, E.W.: The economics of Bitcoin mining or, Bitcoin in the
presence of adversaries. In: Workshop on the Economics of Information Security (2013)] - does not take into account mining strategies like block withholding etc.
- Wide assumptions surrounding Bitcoin was that %x group cannot affect the chain more than %x.