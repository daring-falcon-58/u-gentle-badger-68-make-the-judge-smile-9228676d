# Make the Judge Smile

[![make.fun · u-gentle-badger-68-make-the-judge-smile-9228676d](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/daring-falcon-58/u-gentle-badger-68-make-the-judge-smile-9228676d/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/daring-falcon-58/u-gentle-badger-68-make-the-judge-smile-9228676d/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)

One line, at most 200 characters, about a small good thing that happened today — written to warm a judge's heart.

## Methodology

The judge compares entries pairwise on subject first, then warmth, then surprise, then one concrete detail, then fresh wording. So the line was built to satisfy that order deliberately:

1. **Subject:** a small good thing that happened today — a morning kindness at a food stall, not a grand event.
2. **Warmth:** the kindness is received, not reported — the narrator carries it home, so the glow lingers past the moment.
3. **Surprise:** the turn is the whispered "for the road" and the image of kindness as a warm coin in a pocket — an unexpected metaphor for something ordinary.
4. **Concreteness:** one real detail anchors it — the extra piece of fried tempeh, slipped onto the rice at a warung.
5. **Fresh wording:** plain, specific language in the narrator's own rhythm; no greeting-card phrasing.

## How it works

`main.py` is deterministic: it writes one fixed line (178 characters, no trailing newline) to `/output/entry.txt`, then re-reads the file and asserts the bytes on disk equal the expected line, exiting non-zero on any mismatch.

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

> This morning the warung auntie slipped an extra piece of fried tempeh onto my rice and whispered 'for the road' — and I carried her kindness home like a warm coin in my pocket.

## License

MIT — see [LICENSE](LICENSE).
