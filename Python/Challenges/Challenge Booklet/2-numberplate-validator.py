#Numberplate validator
import re
import string

letters_list = []
letters = string.ascii_lowercase
letters2 = string.ascii_uppercase
letters_list.extend(letters)
letters_list.extend(letters2)

class checkNumber():
    def __init__(self, number):
        self.number = number
    def check(self):
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        if self.number in numbers:
            return 1
        else:
            return 0

class checkNumberplate():
    def __init__(self, numberplate):
        self.numberplate = numberplate
    def check(self):
        types = []
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        chars = list(self.numberplate)
        for i in chars:
            if i in letters_list:
                types.append("letter")
            elif i in numbers:
                types.append("number")
            else:
                return 0
        if types == ["letter", "letter", "number", "number", "letter", "letter", "letter"]:
            return 1
        else:
            return 0

numberplate = input("Enter a numberplate: ")

validator = checkNumberplate(numberplate)

valid = validator.check()

if valid:
    print("Numberplate is valid")
elif not valid:
    print("Numberplate is not valid")
    print(valid)