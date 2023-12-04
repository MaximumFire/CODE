with open("CODE/Python/AdventOfCode/2023/Day 3/Part 1/input.txt", "r") as f:
    lines = f.readlines()

symbols = ["@", "&", "*", "$", "-", "#", "%", "/", "+", "="]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
total = 0
directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
]

def getNumbersTotal(lines, i, j):
    numbers = []
    for direction in directions:
        x = i + direction[0]
        y = j + direction[1]
        if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[x]):
            continue
        if lines[x][y] in digits:
            if len(numbers) == 0:
                numbers.append([0, [[x, y]]])
                continue
            else:
                noadj = True
                for number in numbers:
                    if [x, y+1] in number[1] and [x, y] not in number[1]:
                        number[1].append([x, y])
                        noadj = False
                    elif [x, y-1] in number[1] and [x, y] not in number[1]:
                        number[1].append([x, y])
                        noadj = False
                if noadj:
                    numbers.append([0, [[x, y]]])
    
    # print(numbers)
    
    for number in numbers:
        number[1].sort()
        for i in range(number[1][-1][1]+1, len(lines[number[1][-1][0]])):
            if lines[number[1][-1][0]][i] in digits and [number[1][-1][0], i] not in number[1]:
                number[1].append([number[1][-1][0], i])
            else:
                break
        for i in range(number[1][0][1]-1, -1, -1):
            if lines[number[1][0][0]][i] in digits and [number[1][0][0], i] not in number[1]:
                number[1].append([number[1][0][0], i])
            else:
                break
    
    # print(numbers)

    for number in numbers:
        number[1].sort()
        tempstr = ""
        for index in number[1]:
            tempstr += lines[index[0]][index[1]]
        number[0] = int(tempstr)

    if len(numbers) != 2:
        return 0
    else:
        return numbers[0][0] * numbers[1][0]      

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "*":
            total += getNumbersTotal(lines, i, j)

print(total)