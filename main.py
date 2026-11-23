"""Entry for make.fun's 'One Line, Zero Use: The Useless Superpower Sprint'.

Writes a single one-line joke about a hilariously useless superpower to
/output/entry.txt, where the competition's gate and judge read it.
"""

from pathlib import Path

LINE = (
    "I can teleport anywhere in the world, as long as it is within "
    "three feet of where I am already standing."
)

OUTPUT_PATH = Path("/output/entry.txt")

# The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace.
MAX_CHARS = 200


def check_line(line: str) -> None:
    """Fail loudly rather than submit an entry the gate would refuse."""
    if not line.strip():
        raise ValueError("entry line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} characters, over {MAX_CHARS}")


def main() -> None:
    check_line(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
