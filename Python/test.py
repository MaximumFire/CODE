thesum = 76
thediff = 38

num1 = 0
num2 = 0

for i in range(0, 100):
    for j in range(0, 100):
        if (i + j) == thesum and (i - j) == thediff:
            num1 = i
            num2 = j


print(num1, num2, (num1 / num2))