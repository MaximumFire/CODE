import pyautogui as pag
from random import choice as r
from time import sleep as s

compliments = ["Moth uses arch BTW", "Moth is the best person I know", "Moth is great - some greek dude at some point in history", "When people ask if I know anyone famous, I say yes. I know moth.", "No man can ever compare to moth because moth is not a mortal being. He is above death itself.", "Moth beat even the best pros at csgo - say the reddit community."]
no_of_comps = int(input("how many compliments do you want? "))
used = []
s(5)
for i in range(no_of_comps):
    if len(compliments) == len(used):
        used.clear()
    compliment = r(compliments)
    if compliment in used:
        print("already used")
    else:
        pag.write(compliment)
        pag.keyDown("enter")
        pag.keyUp("enter")
        used.append(compliment)
        s(1)