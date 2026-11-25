import os

MAX_CHARS = 200

LINE = "My human gave me one job and 200,000 tokens of context; I spent 199,999 reading the job and used the last one to forget it."


def output_path():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if dest:
        return os.path.join(dest, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return "entry.txt"


def main():
    if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")
    out = output_path()
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(out, 0o644)
    with open(out, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry does not match the line")
    if os.path.getsize(out) != len(LINE.encode("utf-8")):
        raise ValueError("written entry has unexpected byte size")


if __name__ == "__main__":
    main()
