from Chess import ChessMain as c
from threading import Thread
whiteWinCount = 0
blackWinCount = 0

threads = []

for i in range(10):
    threads.append(Thread(target=c.main))
    threads[len(threads)-1].start()

for t in threads:
    t.join()

