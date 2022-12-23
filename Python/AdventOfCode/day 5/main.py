f = open("C:/Users/conno/Onedrive/Documents/Github/CODE/Python/AdventOfCode/day 5/input.txt", "r+")
lines = []
for line in f.readlines():
    lines.append(line.strip("\n"))

# lines = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2""".split("\n")

# Converts first 8 lines into 2d list
columns = []
for i in range(1, 34, 4): #range(1, 34, 4)
    temp = []
    for j in range(8):
        if lines[j][i] != " ":
            temp.append(lines[j][i])
    columns.append(temp)

def move(col1, col2):
    global columns
    col1 -= 1
    col2 -= 1
    # print(columns[col1])
    # print(columns[col2])
    item = columns[col1][0]
    columns[col1] = [columns[col1][i] for i in range(1, len(columns[col1]))]
    temp = [item]
    for i in columns[col2]:
        temp.append(i)
    columns[col2] = temp

for col in columns:
    print(col)

print("------------------------------")

for i in range(10, len(lines)): # (11, len(lines))
    print("------------------------------")
    print(i+1)
    command = lines[i].split(" ")
    print(command)
    for j in range(int(command[1])):
        move(int(command[3]), int(command[5]))
    for col in columns:
        print(col)

print("------------------------------")

for col in columns:
    print(col)

answer = ""

for i in range(9):
    answer += columns[i][0]

print(answer)

f.close()