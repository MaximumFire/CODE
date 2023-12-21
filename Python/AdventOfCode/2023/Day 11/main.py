with open("CODE/Python/AdventOfCode/2023/Day 11/input.txt", "r") as f:
    lines  = [line.strip("\n") for line in f.readlines()]

empty_rows = [r for r, row in enumerate(lines) if all(ck == "." for ck in row)]
empty_cols = [c for c, col in enumerate(zip(*lines)) if all(ck == "." for ck in col)]

points = [(r, c) for r, row in enumerate(lines) for c, ck in enumerate(row) if ck == "#"]

total = 0
scale = 1000000


for i, (r1, c1) in enumerate(points):
    for (r2, c2) in points[:i]:
        for r in range(min(r1, r2), max(r1, r2)):
            total += scale if r in empty_rows else 1
        for c in range(min(c1, c2), max(c1, c2)):
            total += scale if c in empty_cols else 1

print(total)
