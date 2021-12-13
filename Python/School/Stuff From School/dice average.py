import random
iterations = int(input("How many times would you like this to run? "))
numbers = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
for i in range(0, iterations):
    roll = random.randint(1, 6)
    numbers[str(roll)] += 1
highest = 0
category = ""
for k in numbers:
    if highest <= numbers[k]:
        highest = numbers[k]
        category = k
print(f"The most frequent number was {category}")
a = input("")
