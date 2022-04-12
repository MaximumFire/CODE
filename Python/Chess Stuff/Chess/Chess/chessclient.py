import ChessEngine as ChessEngine
import pygame as p
from requests import *

URL = "http://127.0.0.1:5000/"

board = get(URL + "board").json()

for row in board:
    print(row)

post(URL + "move/1/6/4/4/4")

board = get(URL + "board").json()

for row in board:
    print(row)