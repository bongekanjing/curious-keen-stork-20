# Forty-One Keys

A single 259-character riddle about a grandfather's labelled keys and the one that has no lock left to fit.

## The text

Forty-one keys hang by my grandfather's door, each labelled in his small square hand. Forty name a room. The last reads only: the one you will want. I have tried all forty, twice each. The house has no lock left. The key is still warm, and it is the only one.

## How to run

```
MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py
```

The text lives in `main.py` as the module-level constant `ENTRY`, so the script needs no sibling imports and runs under `python3 -P -s` (which drops the script's own directory from `sys.path`). It strips the text, asserts it is 1-280 characters, writes it to `entry.txt` in the output directory (`$MAKEFUN_OUTPUT_DIR`, default `/output`), re-reads the file to verify, and prints the character count.

[![b](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![r](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/bongekanjing/curious-keen-stork-20/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard)
[![w](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/bongekanjing/curious-keen-stork-20/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard)
