import socket
from threading import Thread
from time import sleep
import select

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

global_data = "4992".encode()

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection, Server Started")

threads = []
idCount = 0

def threaded_client(conn, id):

    global global_data

    conn.settimeout(5)

    while True:
        try:
            data = conn.recv(4096)
            global_data = data
            conn.send(global_data)
        except TimeoutError:
            break

    print("Connection closing...")
    conn.close()

    for thread in threads:
        if thread[1] == id:
            threads.remove(thread)

    print("Thread Removed From List")

sleep(5)

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    thread = Thread(target=threaded_client, args=(conn, idCount))
    thread.start()

    threads.append((thread, idCount))
    idCount += 1

    if len(threads) == 0:
        print("No connections... Stopping server.")
        break