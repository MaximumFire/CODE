import socket

class Test:
    def __init__(self, name):
        self.name = name

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(data)
        except Exception as e:
            print(e)

    def receive(self):
        try:
            data = self.client.recv(4096)
            return data
        except Exception as e:
            print(e)


n = Network()

n.connect()

n.send(str.encode("hii"))

print(n.receive().decode())