with open("CODE/Python/AdventOfCode/2022/day 6/input", "r+") as f:
    data = f.read()

for i in range(len(data)):
    if len(set(data[i:i+14])) == 14:
        print(i+14)
        break