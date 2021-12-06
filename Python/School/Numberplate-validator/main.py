import classes
from classes import *

numberplate = input("Enter a numberplate: ")

validator = checkNumberplate(numberplate)

valid = validator.check()

if valid:
    print("Numberplate is valid")
elif not valid:
    print("Numberplate is not valid")
    print(valid)