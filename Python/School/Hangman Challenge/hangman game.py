import os
import time

correctGuesses = 0 #number of correct guesses
incorrectGuesses = 0 #number of incorrect guesses
running = True
guesses = [] #a list that contains all of the letters that have been guesses. this prevents you from just guessing something over and over again
frequency = {} #the frequency of all the letters in the word
timesGuessUsed = {} #the number of times a guess has been used, does a similar job to guesses
graphicCount = 0 #keeps track of what image should be displayed
wordList = [] #stores the word in a list as individual letters
hiddenWordList = [] #keeps track of which letters have been found

def graphic(number): #a function that displays the hangman images/graphics
    if number == 1:
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print("      ")
        print(" _____")
    elif number == 2:
        print("      ")
        print("      ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|_____")
    elif number == 3:
        print("")
        print("______")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|_____")
    elif number == 4:
        print("      ")
        print("______")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|\____")
    elif number == 5:
        print("      ")
        print("______")
        print("|/    ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|\____")
    elif number == 6:
        print("      ")
        print("______")
        print("|/   |")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|\____")
    elif number == 7:
        print("      ")
        print("______")
        print("|/   |")
        print("|    O")
        print("|     ")
        print("|     ")
        print("|\____")
    elif number == 8:
        print("      ")
        print("______")
        print("|/   |")
        print("|    O")
        print("|    |")
        print("|     ")
        print("|\____")
    elif number == 9:
        print("      ")
        print("______")
        print("|/   |")
        print("|   \O/")
        print("|    |")
        print("|     ")
        print("|\____")
    elif number == 10:
        print("      ")
        print("______")
        print("|/   |")
        print("|   \O/")
        print("|    |")
        print("|    ^")
        print("|\____")
    elif number == 11:
        print("      ")
        print("______")
        print("|/   |")
        print("|    _")
        print("|   /|\ ")
        print("|    ^")
        print("|\____O")       

word = input("Enter the word that will be guessed: ") #user 1 inputs a word
length = len(word) #gets the length of user 1's word
os.system("cls") #clears the screen. most elegant way i found to do it in python
print(f"The word is {length} letters long.")
for i in word: #a loop that gives frequency its values
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

for j in word: #a loop that gives timesGuessUsed its values
    if j in timesGuessUsed:
        timesGuessUsed[j] += 0
    else:
        timesGuessUsed[j] = 0

for k in word: #a loop that makes 2 lists. It makes one that looks like ["e", "y", "e"] and one that looks like ["_", "_", "_"]
    wordList.append(k)
    hiddenWordList.append("_")

while running == True: #while loop that keeps going until either the person guesses the word or they guess incorrectly 11 times
    lettersCorrect = 0 #variable for the below loop
    for m in hiddenWordList: #sets lettersCorrect to be the number of letters that the person has currently gotten correct
        if m != "_":
            lettersCorrect = lettersCorrect + 1
    if correctGuesses == length: #if the player wins
        running = False
        won = True
        break #exit while loop
    elif incorrectGuesses == 11: #if the player loses
        running = False
        won = False
        break #exit while loop
    elif lettersCorrect == length: #checks if a player has won before running the rest of loop
        running = False
        won = True
        break
    else:
        guess = input("Guess a letter: ") #user inputs a letter
        lowerGuess = guess.lower() #converts the letter into lowercase to remove potential errors
        if lowerGuess in word: #checks if the letter is in the word. Returns Boolean
            if lowerGuess == word:
                won = True
                break
            else:
                if lowerGuess not in guesses: #checks if you haven't used a letter before
                    guesses.append(lowerGuess) #adds letter to guesses list
                    correctGuesses = correctGuesses + 1 #adds 1 to correct guesses
                    print(f"{lowerGuess} was in the word.")
                    timesGuessUsed[lowerGuess] = timesGuessUsed[lowerGuess] + 1 #sets timesGuessUsed to be 1 more for that guess
                elif lowerGuess in guesses: #checks if you have used a letter before
                    if frequency[lowerGuess] > 1: #checks if there is more than one of the guessed letter
                        if timesGuessUsed[lowerGuess] >= frequency[lowerGuess]: #checks if you have used the letter the maximum amount of times
                            print("You have already correctly guessed that letter.")
                            incorrectGuesses = incorrectGuesses + 1 #adds 1 to incorrect guesses
                            graphicCount = graphicCount + 1 #adds 1 to graphicCount so it displays the right graphic
                        elif timesGuessUsed[lowerGuess] < frequency[lowerGuess]: #checks if you have used the letter less than the maximum amount of times
                            timesGuessUsed[lowerGuess] = timesGuessUsed[lowerGuess] + 1 #adds 1 to the times you have used a certain letter
                            correctGuesses = correctGuesses + 1 #adds 1 to correct guesses
                            print(f"{lowerGuess} was in the word.")
                    else:
                        print("You have already correctly guessed that letter.")
                        incorrectGuesses = incorrectGuesses + 1 #adds 1 to incorrect guesses
                        graphicCount = graphicCount + 1 #adds 1 to graphicCount in order to display the correct one
                count = 0 #variable for the below loop
                for l in wordList: #loop that changes values in hiddenWordList from "_" to the letter
                    if l == lowerGuess:
                        hiddenWordList[count] = l
                    count = count + 1
        else:
            incorrectGuesses = incorrectGuesses + 1 #adds 1 to incorrect guesses
            print(f"{lowerGuess} was not in the word.")
            graphicCount = graphicCount + 1 #adds 1 to graphicCount in order to display the correct one
        graphic(graphicCount) #displays the graphic after the end of each guess
        print(hiddenWordList) #prints the correctly guessed letters, e.g. _ _ _ e _ o
    
if won == True: #checks if you won
    print(f"Well Done! You correctly guessed that the word was: {word}.")
elif won == False: #checks if you lost
    print(f"Oh no! You lost, the word was: {word}.")
    graphic(11) #discplays the losing graphic

a = input("") #keeps the python window open when double clicking from file explorer. Not necisarry if you are using IDLE.