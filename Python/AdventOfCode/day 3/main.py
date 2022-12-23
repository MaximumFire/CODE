import string

f = open("CODE/Python/AdventOfCode/day three/input.txt", "r+")
lines = f.readlines()

priority_sum = 0

priority = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

# lines = [
#     "vJrwpWtwJgWrhcsFMMfFFhFp\n",
#     "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
#     "PmmdzqPrVvPwwTWBwg\n",
#     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
#     "ttgJtRGJQctTZtZT\n",
#     "CrZsJsPPZsGzwwsLwLmpwMDw\n"
# ]

found = False
groups = []
group = []

for i in range(len(lines)):
    group.append(lines[i][:-1])
    if (i % 3) == 2:
        groups.append(group)
        group = []

for group in groups:
    found = False
    priority_temp = 0

    for i in group[0]:
        for j in group[1]:
            for k in group[2]:
                if i == j and j == k and i == k and not found:
                    if i in string.ascii_uppercase:
                        priority_temp = priority[i.lower()]+26                    
                    else:
                        priority_temp = priority[i]

    priority_sum += priority_temp

print(priority_sum)

f.close()