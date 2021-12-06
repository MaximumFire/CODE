from time import sleep as s
from datetime import datetime
from random import choice as ch

sentences = ["The quick brown fox jumped over the lazy dog."]# "The lazy duck waddled over to the water.", "The excitable child ran around the park."]

while True:
    print("You will be given a sentence to type.\nYou will need to press Enter to confirm your sentence.\nIf you have made a mistake, you will need to re-type the sentence.\nYour time will be given to you at the end.")
    start = input("Press Enter to start.")
    s(1)
    print("3")
    s(1)
    print("2")
    s(1)
    print("1")
    s(1)
    print("GO!")
    start_time = datetime.now().time().second
    chosen_sentence = ch(sentences)
    print(f"Your sentence is : {chosen_sentence}")
    attempt = input("Enter your sentence here : ")
    if attempt == chosen_sentence:
        end_time = datetime.now().time().second
        score = end_time - start_time
        if score < 0:
            score += 60 
        print(f"Congratulations! You successfully entered the sentence in : {score} seconds!")
        chars_per_second = len(chosen_sentence) / score
        chars_per_minute = chars_per_second * 60
        print(f"Your average words per minute was : {int(round(chars_per_minute)/5)}") 
    else:
        print(f"Your attempt was not correct.")
    choice = input("Would you like to try again? (y/n): ")
    if choice == "y":
        continue
    else:
        break