from random import randint, choice

s = [chr(randint(ord("a"), ord("z"))) for _ in range(1000)]
processed = []
while len(processed) < 100:
    i = randint(0, len(s) - 1)
    if i not in processed:
        processed.append(i)
        s[i] = choice(["heavy", "metal"])

with open("4.txt", "w", encoding="utf-8") as f:
    f.write("".join(s))
