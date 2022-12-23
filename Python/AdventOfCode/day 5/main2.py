f = open("C:/Users/conno/Onedrive/Documents/Github/CODE/Python/AdventOfCode/day 5/input.txt", "r+")
lines = []
for line in f.readlines():
    lines.append(line.strip("\n"))

# Converts first 8 lines into 2d list
columns = []
for i in range(1, 34, 4): #range(1, 34, 4)
    temp = []
    for j in range(8):
        if lines[j][i] != " ":
            temp.append(lines[j][i])
    columns.append(temp)

def move(col1, col2, height):
    global columns
    col1 -= 1
    col2 -= 1
    items = []
    for i in range(height):
        items.append(columns[col1][i])
    columns[col1] = [columns[col1][i] for i in range(height, len(columns[col1]))]
    for i in columns[col2]:
        items.append(i)
    columns[col2] = items

for i in range(10, len(lines)):
    command = lines[i].split(" ")
    move(int(command[3]), int(command[5]), int(command[1]))

answer = ""

for i in range(9):
    answer += columns[i][0]

print(answer)

f.close()