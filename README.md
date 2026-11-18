# The World in One Day — November 17, 2026

A single-image newspaper front page summarizing the world news of
Tuesday, November 17, 2026, built for the make.fun news-image bounty.

## What the image shows
- Main story: LPG tanker Tara Gas ablaze in the Strait of Hormuz; crew evacuated.
- Second story: Quad leaders (USA, Japan, Australia, India) meet in Manila;
  Washington responds to Iran's "dirty bomb" threat.
- Panels: Crimea/Kerch Bridge strikes; COP31 fossil-fuel fight in Antalya;
  Wall Street slide and Nvidia results; Ebola record spread in Congo;
  storms flooding California and Florida; Voyager 1 nearing one light-day;
  Pulisic's bicycle kick as the USA beat Haiti 2-0.

## How it works
`main.py` copies the bundled `entry.png` to the output path
(`/output/entry.png` by default, or `$ENTRY_OUTPUT`). Deterministic,
no network. `build_entry.py` is the script that originally composed
the page (Pillow typesetting over generated panel art).

## License
MIT — see LICENSE.
