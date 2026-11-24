import os

# One Letter for Your Day: the letter is the whole entry.
#
# The letter is "Z", standing for "zombie" — a day spent shambling
# through everything half-asleep, brain switched off, running on
# caffeine and muscle memory. Z is the sharpest single-letter day:
# it calls up an instant picture (the zombie shuffle), it is funny
# the moment you hear it, and it is honest — everyone has had a
# zombie day. The letter fits its word exactly: Z is zombie's own
# initial, and no other letter says "zombie".
#
# The gate requires exactly 1 character, UTF-8, not only
# whitespace, so the program writes one byte, "Z", with no
# trailing newline and nothing else.
LETTER = "Z"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Guard the gate: the entry is only valid if the file holds
    # exactly one character. Read it back and fail loudly rather
    # than ever submitting a blank or multi-character file.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if len(written) != 1 or written != LETTER:
        raise ValueError("entry.txt must hold exactly one letter, got %r" % written)


if __name__ == "__main__":
    main()
