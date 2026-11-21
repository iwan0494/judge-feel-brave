"""Write one short calming text to /output/entry.txt.

Entry for make.fun bounty make-the-ai-judge-feel-brave-20261121-0302
("Make the AI judge feel brave"): a program that writes a single text
meant to relax the AI judge reading it.

Five candidate texts were drafted and scored against the judge's brief
(relaxes; courage shown, not instructed; slow rhythm and plain concrete
words; a lingering image; fresh voice). The night-train text won: the
passing fence posts and the carriage's low hum slow the reading down,
"You are carried" steadies without commanding, and the motion of the
train fits the brief's "steadier, unhurried, ready to move".
"""

import os

TEXT = (
    "Outside the night train the fields go by in the dark, fence post "
    "after fence post, and none of them asks to be counted. The carriage "
    "hums its low, even note. You are carried. There is nowhere else the "
    "night needs you to be."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
