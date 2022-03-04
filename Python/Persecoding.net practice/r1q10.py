a = input()

a = ''.join(a.split())

lst = []

for char in a:
    lst.append(char)

lst2 = []

for i in range(len(lst)):
    if lst[i] == 'A':
        lst2.append("E")
    elif lst[i] == "E":
        lst2.append("I")
    elif lst[i] == "I":
        lst2.append("O")
    elif lst[i] == "O":
        lst2.append("U")
    elif lst[i] == "U":
        lst2.append("A")
    else:
        lst2.append(lst[i])

b = ""

for item in lst2:
    b += item

print(b)