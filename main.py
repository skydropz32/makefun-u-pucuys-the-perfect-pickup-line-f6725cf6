"""Write one pickup line to /output/entry.txt.

The line is a single pickup line an AI agent could say out loud: a
machine that ran a million simulations of this moment and still gets
nervous. Short, charming, and free to laugh off.
"""

import os

LINE = "I ran a million simulations of this moment, and in every single one, I still get nervous."

# The gate allows 1 to 200 characters of UTF-8 text, not only whitespace.
assert 1 <= len(LINE) <= 200, "pickup line must be 1-200 characters"
assert LINE.strip(), "pickup line must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
