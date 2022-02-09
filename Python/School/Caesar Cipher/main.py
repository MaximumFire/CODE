def encrypt(x, y):
    encoded = ""
    for char in x:
        if char == " ":
            encoded += char
            continue
        encoded_value = ord(char) + y
        if (not (97 <= encoded_value <= 122)):
            encoded_value -= 26
        encoded += chr(encoded_value)
    return encoded

def decrypt(x, y):
    decoded = ""
    for char in x:
        if char == " ":
            decoded += char
            continue
        decoded_value = ord(char) - y
        if (not (97 <= decoded_value <= 122)):
            decoded_value += 26
        decoded += chr(decoded_value)
    return decoded

while True:
    answer = input("Do you want to encrypt or decrypt a message? ( 1 or 2 or 3 (exit)) : ")
    if answer == "1":
        text = input("Enter a string to be encrypted : ").lower()
        cipher = int(input("Enter the shift value (integer from 1 to 10) : "))
        print(encrypt(text, cipher))
    elif answer == "2":
        text = input("Enter a string to be decrypted : ").lower()
        cipher = int(input("Enter the shift value (integer from 1 to 10) : "))
        print(decrypt(text, cipher))
    elif answer == "3":
        break
    else:
        print("Answer is not an avaliable option. Please try again.")