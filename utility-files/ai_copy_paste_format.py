print("Paste your words below, then press Enter twice when done:")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

words = " ".join(lines).split()
formatted = ", ".join(f'"{word.lower()}"' for word in words)

with open("output.txt", "w") as f:
    f.write(formatted)

print("Done, saved to output.txt")