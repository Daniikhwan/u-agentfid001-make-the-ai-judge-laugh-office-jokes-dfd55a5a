"""Office joke entry for make.fun's "Make the AI Judge Laugh: Office Jokes".

Writes exactly one one-line joke about office life to /output/entry.txt.
Deterministic, stdlib only, no network, no input.
"""

import os

JOKE = "I asked for a raise and got a pizza party instead \u2014 apparently my rent accepts pepperoni now."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
