import random
data = input("Enter a message to encrypted: ")
key = input("Enter the key to encrypt it with (leave blank for random 256 char string): ")
if key == "":
    for i in range(256):
        key = key + chr(random.randint(65, 91))
lst = []
average_value = 0
total = 0
for char in key:
    total += ord(char)
average_value = total // len(key)
for char in data:
    lst.append(ord(char))
result = ""
for num in lst:
    result = result + chr((num + average_value) // 2)
print(result)
with open("C:\\Users\\conno\\OneDrive\\Documents\\GitHub\\CODE\\Python\\Encryption-Decryption\\AverageCharacter\\result.txt", "w+") as f:
    f.write(result)
with open("C:\\Users\\conno\\OneDrive\\Documents\\GitHub\\CODE\\Python\\Encryption-Decryption\\AverageCharacter\\data.txt", "w+") as f:
    f.write(data)
with open("C:\\Users\\conno\\OneDrive\\Documents\\GitHub\\CODE\\Python\\Encryption-Decryption\\AverageCharacter\\key.txt", "w+") as f:
    f.write(key)