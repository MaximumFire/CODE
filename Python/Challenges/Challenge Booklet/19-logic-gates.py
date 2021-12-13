#Logic Gates
def OR(x, y):
    if x == 1 and y == 1:
        return 1
    elif x == 1 and y == 0:
        return 1
    elif x == 0 and y == 1:
        return 1
    else:
        return 0

def AND(x, y):
    if x == 1 and y == 1:
        return 1
    else:
        return 0

def NOT(x):
    if x == 1:
        return 0
    else:
        return 1

def XOR(x, y):
    if x == 1 and y == 1:
        return 0
    elif x == 1 and y == 0:
        return 1
    elif x == 0 and y == 1:
        return 1
    else:
        return 0

def NAND(x, y):
    if x == 1 and y == 1:
        return 0
    elif x == 1 and y == 0:
        return 1
    elif x == 0 and y == 1:
        return 1
    else:
        return 1
    
def NOR(x, y):
    if x == 0 and y == 0:
        return 1
    else:
        return 0

choice = input("What gate would you like an answer to (OR, AND, NOT, XOR, NAND, NOR): ")
if choice == "OR":
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    print(OR(x, y))
elif choice == "AND":
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    print(AND(x, y))
elif choice == "NOT":
    x = int(input("Enter the value: "))
    print(NOT(x))
elif choice == "XOR":
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    print(XOR(x, y))
elif choice == "NAND":
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    print(NAND(x, y))
elif choice == "NOR":
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))
    print(NOR(x, y))