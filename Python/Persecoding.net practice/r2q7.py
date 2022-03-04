grid = []
n = int(input())
m = int(input())

for i in range(m):
    temp = input().split(" ")
    for char in temp: temp[temp.index(char)] = int(char)
    grid.append(temp)

currentMax = 0
isrow0 = False
iscol0 = False
isrowmtake1 = False
iscolntake1 = False


def checkdiags(i, j):
    global currentMax, iscol0, isrow0, iscolntake1, isrowmtake1, grid
    isrow0 = False
    iscol0 = False
    isrowmtake1 = False
    iscolntake1 = False
    if i == 0:
        isrow0 = True
    if i == (m-1):
        isrowmtake1 = True
    if j == 0:
        iscol0 = True  
    if j == (n-1):
        iscolntake1 = True
    if isrow0:
        if iscol0:
            if (grid[i+1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i+1][j+1] * grid[i][j]
        elif iscolntake1:
            if (grid[i+1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i+1][j-1] * grid[i][j]
        else:
            if (grid[i+1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i+1][j+1] * grid[i][j]
            if (grid[i+1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i+1][j-1] * grid[i][j]
    elif isrowmtake1:
        if iscol0:
            if (grid[i-1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j+1] * grid[i][j]
        elif iscolntake1:
            if (grid[i-1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j-1] * grid[i][j]
        else:
            if (grid[i-1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j+1] * grid[i][j]
            if (grid[i-1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j-1] * grid[i][j]
    else:
        if iscol0:
            if (grid[i-1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j+1] * grid[i][j]
            if (grid[i+1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j+1] * grid[i][j]
        elif iscolntake1:
            if (grid[i-1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j-1] * grid[i][j]
            if (grid[i+1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j-1] * grid[i][j]
        else:
            if (grid[i-1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j+1] * grid[i][j]
            if (grid[i-1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j-1] * grid[i][j]
            if (grid[i+1][j+1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j+1] * grid[i][j]
            if (grid[i+1][j-1] * grid[i][j]) > currentMax:
                currentMax = grid[i-1][j-1] * grid[i][j]

for i in range(m):
    for j in range(n):
        checkdiags(i, j)

print(currentMax)