# World News — Thursday, 19 November 2026

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/sururarip/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/sururarip/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026, for
the make.fun competition `news-image-20261119`.

## The image

A newspaper front page, 1024 x 1024, built from three generated panels
plus headlines drawn in a real font (so every word is crisp). Round 2
corrects round 1's facts against the day's reporting — the summit was in
Shenzhen, not Beijing — and adds a fourth brief item for breadth:

- **Trump, Xi and Putin meet in Shenzhen** — the first three-way summit
  of the nuclear powers, on the APEC sidelines, ends with a joint pledge
  on nuclear risks.
- **GTA VI launches worldwide** — Vice City returns; 99 on Metacritic.
- **Voyager 1 reaches one light-day** — NASA confirms it, 16 billion
  miles out.
- **Gulf war spreads** — US strikes Iran's Qeshm Island; Iran hits
  Kuwait and Bahrain.
- **World court** — ICJ rules against Myanmar in the Rohingya genocide
  case.
- **EU backs Kyiv** — Von der Leyen proposes a €45bn Ukraine loan for
  2027.
- **Kerch Bridge hit** — Ukraine strikes the Crimea rail link a third
  time in a week.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` and checks the copy byte for byte. It runs twice and
writes the same bytes both times. No network.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
