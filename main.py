#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a newspaper front page
summing up Thursday 19 November 2026 — the Trump-Xi-Putin trilateral in
Beijing, the US-Iran strikes in the Gulf, GTA VI's worldwide launch,
Voyager 1's one-light-day milestone, the EU's EUR 45bn Ukraine loan and
the ICJ's Myanmar genocide ruling. This program copies it to /output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)

shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
assert (OUT / "entry.png").stat().st_size == (HERE / "entry.png").stat().st_size
