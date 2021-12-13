#Factorial Finder
starting = int(input("Enter a starting number: "))
counter = 0
results = []
total = 1
results.append(starting)
while True:
    counter += 1
    result = starting - counter
    if 0 >= result:
        break
    else:
        results.append(result)
for number in results:
    total = total * number
print(f"The factorial of {starting} is: {total}")