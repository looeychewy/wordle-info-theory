# quick claude program to sort unsorted list of 5 letter words from .txt and output .csv

import sys
import csv


def load_words(source) -> list[str]:
    """Read lines from a file-like object or path string."""
    if isinstance(source, str):
        with open(source, "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = source.readlines()
    return lines


def clean_and_validate(lines: list[str]) -> list[str]:
    """Strip whitespace, lowercase, deduplicate, and keep only 5-letter alpha words."""
    seen = set()
    words = []
    for line in lines:
        for token in line.split():           # handles multiple words per line
            word = token.strip().lower()
            if len(word) == 5 and word.isalpha() and word not in seen:
                seen.add(word)
                words.append(word)
    return words


def write_csv(words: list[str], dest) -> None:
    """Write sorted words to a CSV with index, word, and first-letter columns."""
    words.sort()
    if isinstance(dest, str):
        f = open(dest, "w", newline="", encoding="utf-8")
        close_after = True
    else:
        f = dest
        close_after = False

    try:
        writer = csv.writer(f)
        writer.writerow(["#", "word", "first_letter"])
        for i, word in enumerate(words, start=1):
            writer.writerow([i, word, word[0].upper()])
    finally:
        if close_after:
            f.close()

    print(f"✓ {len(words)} unique 5-letter words written.", file=sys.stderr)


def main():
    args = sys.argv[1:]

    # Determine input source
    if args:
        input_source = args[0]
    else:
        input_source = sys.stdin

    # Determine output destination
    if len(args) >= 2:
        output_dest = args[1]
    else:
        output_dest = sys.stdout

    lines = load_words(input_source)
    words = clean_and_validate(lines)

    if not words:
        print("No valid 5-letter words found.", file=sys.stderr)
        sys.exit(1)

    write_csv(words, output_dest)


if __name__ == "__main__":
    main()