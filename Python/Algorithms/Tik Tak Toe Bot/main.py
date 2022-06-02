# A simple game that can be played by 1 person and the computer or 2 people.

board = [" " for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos]

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def isBoardFull(board):
    if board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
        return False
    else:
        return True

def playerMove():
    run = True
    while run:  # Keep looping until we get a valid move
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:  # makes sure we type in a number between 1-9
                if spaceIsFree(move):  # check if the move we choose is valid (no other letter is there already)
                    run = False
                    insertLetter('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # Create a list of possible moves
    move = 0
    
    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move


    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move

    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():

    print("Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)#
        else:
            print('O\'s win this time...')
            break

        
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Game is a Tie! No more spaces left to move.')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s win, good job!')
            break


    if isBoardFull(board):
        print('Game is a tie! No more spaces left to move.')

while True:
    answer = input("Do you want to play again? (Y/N)")
    if answer.lower() == "y" or answer.lower() == "yes":
        board = [" " for x in range(10)]
        print("-----------------------------------")
        main()
    else:
        break