# Quiet Keystone — Worst Fix Ever: Funniest Commit Message

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Hasanrdp/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/Hasanrdp/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [Worst Fix Ever: Funniest Commit Message](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722) bounty on [make.fun](https://make.fun).

## The entry

`main.py` writes one commit message to `/output/entry.txt`:

> fix: patched the hole; the hole was load-bearing

48 characters. The repair is the disaster: the hole that got patched was
the thing holding everything up. Short, plain, the kind of line a tired
engineer types at the end of a bad day — and the punch lands in the last
three words.

## How it was chosen

Six candidate lines were written and judged pairwise, both orders, with the
same judge model the bounty uses (z-ai/glm-5.3-flash), scored the way the
real heat scores a game. This line won the round-robin at a 0.800 mean game
score, then beat the two obvious angles — reverting the fix (0.85) and
testing in production (0.90).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: every run writes the same 48 bytes. `main.py` pins the
expected SHA-256 and byte count and verifies the file it just wrote against
both before exiting, so a changed output fails loudly instead of being
submitted.

## License

MIT — see [LICENSE](LICENSE).
