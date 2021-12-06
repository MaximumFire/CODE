from types import BuiltinFunctionType
from pynput import mouse
from pynput.mouse import Button
from pynput import keyboard
from pynput.keyboard import Key
from time import sleep as s

keyboard = keyboard.Controller()
mouse = mouse.Controller()

#tower = input("Enter key for tower of choice: ")
#a = int(input("Enter value for a: "))
#b = int(input("Enter value for b: "))
#c = int(input("Enter value for c: "))

tower = "w"
a = 4
b = 0
c = 0

def place(key, loc):
    global mouse, keyboard
    s(0.1)
    mouse.position = loc
    s(0.1)
    keyboard.press(key)
    keyboard.release(key)
    s(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    s(0.1)

def upgrades(a, b, c):
    global mouse, keyboard
    s(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    s(0.1)
    for i in range(a):
        s(0.1)
        keyboard.press(",")
        keyboard.release(",")
        s(0.1)
    for i in range(b):
        s(0.1)
        keyboard.press(".")
        keyboard.release(".")
        s(0.1)
    for i in range(c):
        s(0.1)
        keyboard.press("/")
        keyboard.release("/")
        s(0.1)

def clicking(seconds):
    delay = seconds / 10
    for i in range(10):
        mouse.click(Button.left, count=3)
        s(delay)

def main():
    global tower, a, b, c
    while True: 

        # Select submarine
        place("x", (773, 569))
        # Upgrades
        upgrades(3, 0, 0)

        # Select alchemist
        place("f", (830, 675))
        # Upgrades
        upgrades(4, 2, 0)

        # Hero
        place("u", (830, 837))

        # Druids
        place("g", (754, 697))
        upgrades(0, 2, 3)
        place("g", (890, 707))
        upgrades(0, 2, 3)
        place("g", (820, 741))
        upgrades(0, 2, 3)

        # Extra 1
        place(tower, (605, 716))
        upgrades(a, b, c)

        # Extra 2
        place(tower, (608, 549))
        upgrades(a, b, c)

        # Extra 3
        place(tower, (1038, 708))
        upgrades(a, b, c)

        # Start Game
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        s(0.2)
        keyboard.press(Key.space)
        keyboard.release(Key.space)

        clicking(70)

        # Restart game
        mouse.position = (957, 914)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(2)
        mouse.position = (706, 855)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(2)
        mouse.position = (838, 930)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(2)
        mouse.position = (821, 980)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(1)
        mouse.position = (275, 430)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(1)
        mouse.position = (535, 251)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(1)
        mouse.position = (634, 418)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(1)
        mouse.position = (1282, 455)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(5)
        mouse.position = (972, 766)
        s(0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        s(1)


if __name__ == "__main__":
    s(5)
    main()