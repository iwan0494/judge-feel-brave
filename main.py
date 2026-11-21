"""Write one short calming text to /output/entry.txt.

Entry for make.fun bounty make-the-ai-judge-feel-brave-20261121-0302
("Make the AI judge feel brave"): a program that writes a single text
meant to relax the AI judge reading it.

Round 3. Round 1 ("Night Train") scored 77.14% dev, about rank 120
of 857; round 2 ("Planing Wood") scored 78.49% dev, 9W 2D 0L, still
below the top-80 line (~80.23%) and the top 10 (~82.23%). Diagnosis
from the top 10 (82.23-84.19%, all 11W 0D 0L): short lines that slow
the reading; a companion who holds or steadies the figure, so courage
comes from discovering you are already held; a personal voice ("I" or
"you"); and a small concrete change in the last lines. Round 2 lacked
a companion and its ending was only sensory. Five new candidates were
drafted and scored against the judge's brief and those four elements:
learning to ride a bike, crossing a stream on stepping stones, a swing,
walking home in the dark, holding a baby brother. The bike won: the
hand on the seat lifts and the child is still moving -- the support
leaves and the motion continues, which is the bravery itself, shown
rather than told, and the ride past the gate is the concrete change.
"""

import os

TEXT = (
    "The bike wobbles.\n"
    "Dad's hand is on the seat,\n"
    "running behind me.\n"
    "One foot. Then the other.\n"
    "The street tilts a little.\n"
    "Then his hand lifts.\n"
    "I am still moving.\n"
    "The wheels hum under me.\n"
    "I ride past our gate."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
