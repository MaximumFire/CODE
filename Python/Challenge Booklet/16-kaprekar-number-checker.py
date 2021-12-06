#Kaprekar Number Checker
original_number = int(input("Enter a number to be checked: "))
number = original_number ** 2
number2 = 0
left = 0
right = 0
if len(str(number)) > 2:
    if len(str(number)) % 2 != 0:
        left = int((len(str(number)) - 1) / 2)
        right = int((len(str(number)) + 1) / 2)
    else:
        left = int((len(str(number))) / 2)
        right = left
    left2 = str(number)
    left2 = left2[0:left]
    left2 = int(left2)
    right2 = str(number)
    right2 = right2[-right:]
    right2 = int(right2)
    number2 = left2 + right2
else:
    for i in str(number):
        number2 += int(i)
if number2 == original_number:
    print("True")
else:
    print("False")