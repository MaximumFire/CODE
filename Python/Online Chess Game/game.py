import chess

board = chess.Board()

def move(move):
    board.push_san(move)

print(board)

player = "White"

while True:
    print(f"{player} to move.")
    if board.is_checkmate():
        print(f"{player} is in checkmate and has lost.")
        break
    elif board.is_check():
        print(f"{player} is in check.")
    else:
        if player == "White":
            player = "Black"
        else:
            player = "White"  
        choice = input("Enter a move: ")
        if choice == "":
            break
        else:
            try:
                move(choice)
            except ValueError as e:
                print("That is not a valid move.")
                if player == "White":
                    player = "Black"
                else:
                    player = "White"
            print(board)