import random as r
import re

random_number = []
random_string = ""
used_numbers = []
player_numbers = []
choice_list = []
failed = False
won = None

for i in range(0,4):
    number_for_slot = r.randint(0, 9)
    while number_for_slot in used_numbers:
        number_for_slot = r.randint(0, 9)
    used_numbers.append(number_for_slot)
    random_number.append(number_for_slot)

for l in random_number:
    random_string = random_string + str(l)

while True:
    print(random_string)
    cows_and_bulls = {
        "cows": 0,
        "bulls": 0,
    }
    player_numbers = []
    choice_list = []
    failed = False
    choice = input("Enter 'exit' if you want to stop playing or enter a guess to continue: ")
    if choice == 'exit':
        break
    elif choice == random_string:
        won = True
        break
    valid_answer = re.compile("^[0-9][0-9][0-9][0-9]$")
    if valid_answer.match(choice):
        for i in choice:
            if i in player_numbers:
                failed = True
            player_numbers.append(i)
    else:
        failed = True
    if failed:
        print("Your answer did not match the specified format. Please try again.")
        pass
    for j in choice:
        choice_list.append(int(j))
    for k in choice_list:
        if k in random_number:
            cow = True
            actual_pos = random_number.index(k)
            choice_pos = choice_list.index(k)
            if actual_pos == choice_pos and cow:
                cows_and_bulls["bulls"] += 1
            else:
                cows_and_bulls["cows"] += 1
    if cows_and_bulls["cows"] == 1 and cows_and_bulls["bulls"] == 1:
        print("1 bull and 1 cow")
    elif cows_and_bulls["cows"] == 1 and cows_and_bulls["bulls"] != 1:
        print(f"{cows_and_bulls['bulls']} bulls and 1 cow")
    elif cows_and_bulls["cows"] != 1 and cows_and_bulls["bulls"] == 1:
        print(f"1 bull and {cows_and_bulls['cows']} cows")
    else:
        print(f"{cows_and_bulls['bulls']} bulls and {cows_and_bulls['cows']} cows")
if won == True:
    print("Congratulations, you have won the game!")
    print(f"The number was: {random_string}")
else:
    print("Thanks for playing!")