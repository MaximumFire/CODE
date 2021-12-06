data = input("Enter the data to be encoded: ")
asciiList = []
for i in data:
    asciiList.append(str(ord(i)))
for j in asciiList:
    asciiList[asciiList.index(j)] = j[::-1]
for k in asciiList:
    asciiList[asciiList.index(k)] = chr(int(k))
string = "".join(asciiList)
print(string)