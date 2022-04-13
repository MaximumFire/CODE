import threading
import socket
import ChessEngine
from random import randint as r


gs = ChessEngine.GameState()
alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                valid_moves = gs.getValidMoves()
                move = valid_moves[r(0, len(valid_moves))]
                gs.makeMove(move)
                for row in gs.board:
                    print(row)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{input("")}'
        client.send(gs)


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
