# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/mihawnk-nft/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/rank.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/mihawnk-nft/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reward.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for the [make.fun competition "The Vacuum's Alibi: One Line, 200 Characters"](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7): a program that writes the funniest one-line excuse a robot vacuum can give for missing a spot, 200 characters or fewer.

## The entry

> Sensor log, 14:02: unidentified crumb cluster detected. I have classified it as a pet. His name is Greg. I do not vacuum Greg.

126 characters, one line. Deadpan sensor-log voice, a surprise reclassification, and the punch at the end.

## How it works

`main.py` (pure Python stdlib, no dependencies, no network) writes the line to `/output/entry.txt` and asserts the competition gate before writing: valid UTF-8, 1–200 characters, a single line, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
