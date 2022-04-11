import ChessEngine as ChessEngine
import socket, pickle

HOST = "localhost"
PORT = 5000


def send():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    variable = ChessEngine.GameState()
    data_string = pickle.dumps(variable)
    s.send(data_string)
    s.close()
    print("Data sent")


def recieve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print("connected by ", addr)

    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    conn.close()
    print(data_variable.board[0])

send()
recieve()