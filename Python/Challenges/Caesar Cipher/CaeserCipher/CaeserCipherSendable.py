while True:
    # Defines all of the ASCII letters
    letters = [
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        ]

    # Takes the input for whether the user wants to Encode or Decode
    while True:
        choice = input("Encode or Decode? ").lower()
        # Makes sure user inputs a valid option
        if choice == "encode" or choice == "decode":
            break
        else:
            print("Please write \"Encode\" or \"Decode\"")

    # The code of the encode feature
    if choice == "encode":
        # Takes the input of what the user wants to encode
        plainText = input("What text do you want to encode? ").lower()
        # Takes the input of the rotations
        while True:
            # Makes sure user inputs an integer
            try:
                rotations = int(input("How many rotations do you want to have \'Rotates to the right\' "))
                break
            except:
                print("Please input an integer! ")

        textLetters = []
        encodedText = ""
        # Appends all of the letters of the user input separatly into a list
        for x in range(len(plainText)):
            textLetters.append(plainText[x])
        # The loop for rotating the letters
        for x in range(len(textLetters)):
            # Checks whether the character is a puntuation character and ignores it
            if textLetters[x] not in letters:
                encodedText += textLetters[x]
            # If it is a regular letter it starts the rotation process
            else:
                # Finds the index of the letter in the letter list
                index = letters.index(textLetters[x])
                # Repeats for how many rotatons the user chose
                for y in range(rotations):
                    # Adds to the index so its moving up the list
                    index += 1
                    # When the list goes past Z it turns back to A
                    if index == 26:
                        index = 0
                # Adds the encoded letters to a string
                encodedText += letters[index]
        # Prints the finished encoded text and capitlises it   
        print(encodedText.title())

    # The code of the decode feature
    if choice == "decode":
        # Takes the input of the text the user wants to decode
        plainText = input("What text do you want to Decode? ").lower()
        # Defines useful variables
        decodedText = ""
        rotations = 1
        textLetters = []
        decoded = []
        relavent = []
        # Appends all of the letters of the user input separatly into a list
        for x in range(len(plainText)):
            textLetters.append(plainText[x])
        # The loop for rotating the letters in all 26 combonations
        for x in range(26):
            # Checks whether the character is a puntuation character and ignores it
            for x in range(len(textLetters)):
                if textLetters[x] not in letters:
                    decodedText += textLetters[x]
                # If it is a regular letter it starts the rotation process
                else:
                    index = letters.index(textLetters[x])
                    # Rotates the number backwards starting from 1 so its formatted correctly when printed
                    for y in range(rotations):
                        # Takes away from the index so it moves down the list
                        index -= 1
                        # When the index goes past A it goes back to Z
                        if index == -1:
                            index = 25
                    # Adds the decoded letters to a string
                    decodedText += letters[index]
            # Prints the decoded text with its amount of rotations
            print(f"Rot {rotations}: " + decodedText.title())
            decoded.append(decodedText)
            # Adds to the rotations to it rotates more
            rotations += 1
            # Resets the decoded ext for the next amount of rotations
            decodedText = ""
        # The loop for finding the most relevant rotations
        for x in range(26):
            # Opens a text file with all of the words in the dictionary
            file = open("C:\\Users\conno\\Downloads\\CaeserCipher\\Dictionary.txt")
            word = decoded[x]
            first = word.split()[0]
            if first in file.read():
                relavent.append(f"Rot {x + 1}: {decoded[x]}")
            else:
                pass
        if len(relavent) == 0:
            print("There were no relavent solutions found :(")
        else:
            print("The most relavent rotations are:")
            for x in range(len(relavent)):
                print(f"{relavent[x].title()}")
    while True:
        again = input("Would you like to go again? (y/n)").lower()
        if again == "y" or again == "n":
            break
        else:
            print("Please input\'y\' or \'n\'")
    if again == "y":
        pass
    else:
        break
        
