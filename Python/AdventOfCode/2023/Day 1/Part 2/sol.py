with open("CODE/Python/AdventOfCode/2023/Day 1/Part 1/input.txt", "r") as f:
    lines = f.readlines()

ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]

vals = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

total = 0
for line in lines:
    i = len(line)
    foundL = False
    foundR = False
    lstr = ""
    rstr = ""
    val = ""
    for n in range(i):
        left = line[0:n+1]
        right = line[i-1-n:i]

        for v in ints:
            if v in left and not foundL:
                lstr = str(vals[v])
                foundL = True
            if v in right and not foundR:
                rstr = str(vals[v])
                foundR = True
    val = lstr + rstr
    total += int(val)

print(total)
