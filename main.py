"""Write one short calming text to /output/entry.txt.

Entry for make.fun bounty make-the-ai-judge-feel-brave-20261121-0302
("Make the AI judge feel brave"): a program that writes a single text
meant to relax the AI judge reading it.

Round 2. Round 1 ("Night Train") scored 77.14% dev, about rank 120 of
857: one dense paragraph, passive watching, an abstract ending, so its
pacing was too fast and nothing concrete lingered. Diagnosis from the
top 10 (81.94-83.63%): short lines that slow the reading, someone doing
slow skilled hand work so courage is shown through the hands, and a
small concrete change at the end. Five new candidates were drafted and
scored against the judge's brief (relaxes; courage shown, not told;
slow rhythm; a lingering image; fresh voice): planing wood, shelling
beans, washing rice, winding a clock, polishing shoes. Planing wood
won: the repeated draw of the plane slows the reading, the board
turning smooth and warm as skin is the concrete change, and the
finished board is ready for its next use -- steadier, unhurried,
ready to move.
"""

import os

TEXT = (
    "Morning.\n"
    "He draws the plane\n"
    "along the board.\n"
    "One long shaving curls,\n"
    "thin as paper,\n"
    "and falls.\n"
    "He draws it again.\n"
    "The board grows smooth\n"
    "under his hands.\n"
    "By noon the wood\n"
    "is warm as skin."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
