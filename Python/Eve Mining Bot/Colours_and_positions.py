import pyautogui as pt
from time import sleep

while True:
    posXY = pt.position()
    print(posXY)
    sleep(1)