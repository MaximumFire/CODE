a = input()

lst = [] # list of characters from input

for char in a:
    lst.append(char)

x = 0 # no. matches

currentChar = " "
concurrentCount = 0

for i in range(51):
    if lst[i] != currentChar and concurrentCount <= 2:
        currentChar = lst[i]
        if lst[i] == lst[i+1]:
            x += 1
    else:
        concurrentCount += 1
        if concurrentCount >= 2:
            concurrentCount = 0
            currentChar = " "

print(x)