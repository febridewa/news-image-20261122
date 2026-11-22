"""News-image entry for Sunday 22 November 2026.

Copies the bundled front-page image to the grader's output directory.
Python 3.13, standard library only. Deterministic: the same bytes every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")

# Sanity check: the written file must be byte-identical to the bundled image,
# so both grader runs produce exactly the same bytes.
assert (OUT / "entry.png").read_bytes() == (HERE / "entry.png").read_bytes()
