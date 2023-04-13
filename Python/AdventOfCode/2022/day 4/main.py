f = open("C:/Users/conno/Onedrive/Documents/Github/CODE/Python/AdventOfCode/day 4/input.txt", "r+")
lines = []
for line in f.readlines():
    lines.append(line.strip("\n"))

# lines = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

total_count = 0

# split on , to create 2 ranges [range1, range2]
for i in range(len(lines)):
    lines[i] = lines[i].split(",")

# split each range on - to create 2 pairs of numbers [[min, max], [min, max]]
for i in range(len(lines)):
    for j in range(2):
        lines[i][j] = lines[i][j].split("-")

# make each string representing a number an integer
for i in range(len(lines)):
    for j in range(2):
        for k in range(2):
            lines[i][j][k] = int(lines[i][j][k])

def check_for_overlap(pairs): # [[1, 2], [2, 4]]
    range_one = [i for i in range(pairs[0][0], pairs[0][1]+1)]
    range_two = [i for i in range(pairs[1][0], pairs[1][1]+1)]

    for x in range_one:
        for y in range_two:
            if x == y:
                return True

# checking for complete overlap
# for i in range(len(lines)):
#     if lines[i][0][0] <= lines[i][1][0] and lines[i][0][1] >= lines[i][1][1]:
#         total_count += 1
#     elif lines[i][1][0] <= lines[i][0][0] and lines[i][1][1] >= lines[i][0][1]:
#         total_count += 1

# checking for partial or full overlap
for pairs in lines:
    if check_for_overlap(pairs=pairs):
        total_count += 1

# print([lines[i] for i in range(5)])
print(total_count)

f.close()