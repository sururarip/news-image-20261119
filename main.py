#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a newspaper front
page summing up Thursday 19 November 2026 — the Trump-Xi-Putin
trilateral in Shenzhen (APEC sidelines), the US strike on Iran's Qeshm
Island and Iran's attacks on Kuwait and Bahrain, the ICJ ruling against
Myanmar in the Rohingya genocide case, the EU's proposed EUR 45bn
Ukraine loan, Ukraine's third Kerch Bridge strike of the week, GTA VI's
worldwide launch, and Voyager 1's one-light-day milestone. This program
copies it to /output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)

SRC = HERE / "entry.png"
DST = OUT / "entry.png"

shutil.copyfile(SRC, DST)
assert DST.stat().st_size == SRC.stat().st_size
assert hashlib.sha256(DST.read_bytes()).hexdigest() == hashlib.sha256(
    SRC.read_bytes()
).hexdigest()
