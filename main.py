import os

LINE = "This morning the warung auntie slipped an extra piece of fried tempeh onto my rice and whispered 'for the road' — and I carried her kindness home like a warm coin in my pocket."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read self-check: the bytes on disk must equal the expected line.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise SystemExit(1)
    if not (1 <= len(written.decode("utf-8")) <= 200):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
