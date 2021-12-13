#Fruit Slot Machine
from random import choice as r

symbols = ["🍒", "🔔", "🍋", "🍊", "⭐", "💀"]
credit = 100
cost = 20
slots = []

while True:
    slots = []
    if credit <= 0:
        print(f"You have: £{credit/100} :left! You can't play anymore!")
        break
    else:
        print(f"You have: £{credit/100} :left!")
        choice = input("Do you want to roll or quit? (r/q): ")
        if choice == "r":
            credit -= 20
            for i in range(3):
                slots.append(r(symbols))
            if slots[0] == slots[1] == slots[2]:
                print(slots)
                if slots[0] == "🔔":
                    print(f"You got 3 bells! You win £5!")
                    credit += 500
                    continue
                elif slots[0] == "💀":
                    print(f"You got 3 skulls! You lose £{credit/100}!")
                    credit -= credit
                    continue
                else:
                    print(f"You got 3 the same! You win £1!")
                    credit += 100
                    continue
            elif slots[0] == slots[1] or slots[0] == slots[2] or slots[1] == slots[2]:
                print(slots)
                if slots[0] == "💀" and slots[1] == "💀":
                    print(slots)
                    print(f"You got 2 skulls! You lose £1!")
                    credit -= 100
                    continue
                elif slots[0] == "💀" and slots[2] == "💀":
                    print(slots)
                    print(f"You got 2 skulls! You lose £1!")
                    credit -= 100
                    continue
                elif slots[1] == "💀" and slots[2] == "💀":
                    print(slots)
                    print(f"You got 2 skulls! You lose £1!")
                    credit -= 100
                    continue
                else:
                    print(f"You got 2 the same! You win 50p!")
                    credit += 50
                    continue
            else:
                print(slots)
        elif choice == "q":
            break