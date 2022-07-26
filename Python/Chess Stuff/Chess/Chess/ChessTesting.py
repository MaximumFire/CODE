import requests as r

board = r.get("http://127.0.0.1:5000/board")

print(board.json())


