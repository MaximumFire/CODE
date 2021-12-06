import chess
import socket
import threading

board = chess.Board()

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

player = ""

def receive():
    global player
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message == 'WHITE':
                player = "White"
            elif message == 'BLACK':
                player = "Black"
            else:
                return message
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

def main():
    print(board)
    global player
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
            client.send(input("Enter a move: ").encode("ascii"))
            choice = receive()
            if choice == "":
                break
            else:
                try:
                    board.push_san(choice)
                except ValueError as e:
                    print("That is not a valid move.")
                    if player == "White":
                        player = "Black"
                    else:
                        player = "White"
                print(board)

receive()
game_thread = threading.Thread(target=main)
game_thread.start()
game_thread.join()