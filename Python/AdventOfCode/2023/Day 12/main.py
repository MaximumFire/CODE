with open("CODE/Python/AdventOfCode/2023/Day 12/test.txt", "r") as f:
    data = [row.split(" ") for row in f.read().splitlines()]

for i in range(len(data)):
    data[i][1] = [int(x) for x in data[i][1].split(",")]

print(data)