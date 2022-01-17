import requests as r
from time import sleep as s
from Chess import Engine as Engine
import threading

nickname = input("Enter a nickname: ")

BASE = "http://127.0.0.1:5000/"
BOARD = BASE + "board"
SETUP = BASE + "setup"
GAME_INFO = BASE + "gameinfo"

GAME_ID = r.get(SETUP)
r.post(SETUP, {"nickname": nickname, "id": GAME_ID})

def get_game_data():
    
