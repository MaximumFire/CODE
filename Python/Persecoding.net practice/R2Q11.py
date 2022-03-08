def letterornumberToIndex(x):
    if x == "a":
        return 0
    elif x == "b":
        return 1
    elif x == "c":
        return 2
    elif x == "d":
        return 3
    elif x == "e":
        return 4
    elif x == "f":
        return 5
    elif x == "g":
        return 6
    elif x == "h":
        return 7
    elif x == "1":
        return 7
    elif x == "2":
        return 6
    elif x == "3":
        return 5
    elif x == "4":
        return 4
    elif x == "5":
        return 3
    elif x == "6":
        return 2
    elif x == "7":
        return 1
    elif x == "8":
        return 0

def mvleft(x, y):
    global board, moves
    if board[x][y] == "B":
        if board[x+1][y+1] == "":
            board[x+1][y+1] = "B"
            board[x][y] = ""
        else:
            if board[x+1][y+1] != board[x][y]:
                board[x+2][y+2] = "B"
                board[x][y] = ""
                board[x+1][y+1] = ""
            
    else:
        if board[x-1][y-1] == "":
            board[x-1][y-1] = "W"
            board[x][y] = ""
        else:
            if board[x-1][y-1] != board[x][y]:
                board[x-2][y-2] = "W"
                board[x][y] = ""
                board[x-1][y-1] = ""

def mvright(x, y):
    global board, moves
    if board[x][y] == "B":
        if board[x+1][y-1] == "":
            board[x+1][y-1] = "B"
            board[x][y] = ""
        else:
            if board[x+1][y-1] != board[x][y]:
                board[x+2][y-2] = "B"
                board[x][y] = ""
                board[x+1][y-1] = ""
            
    else:
        if board[x-1][y+1] == "":
            board[x-1][y+1] = "W"
            board[x][y] = ""
        else:
            if board[x-1][y+1] != board[x][y]:
                board[x-2][y+2] = "W"
                board[x][y] = ""
                board[x-1][y+1] = ""

def displayboard(board):
    for row in board:
        temp = ""
        for cell in row:
            if cell == "":
                temp += "."
            elif cell == "B":
                temp += "b"
            elif cell == "W":
                temp += "w"
        print(temp)

board = [["", "B", "", "B", "", "B", "", "B"],
         ["B", "", "B", "", "B", "", "B", ""],
         ["", "B", "", "B", "", "B", "", "B"],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["W", "", "W", "", "W", "", "W", ""],
         ["", "W", "", "W", "", "W", "", "W"],
         ["W", "", "W", "", "W", "", "W", ""]]


n = int(input())
moves = []

for i in range(n):
    moves.append(input())

for i in range(len(moves)):
    temp = []
    subi = 0
    for char in moves[i]:
        if subi != 2:
            temp.append(letterornumberToIndex(char))
        else:
            temp.append(char)
        subi += 1
    moves[i] = temp

for move in moves:
    if move[2] == "L":
        mvleft(move[1], move[0])
    elif move[2] == "R":
        mvright(move[1], move[0])

displayboard(board)