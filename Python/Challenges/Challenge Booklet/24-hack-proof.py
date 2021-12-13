#hack proof
import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

def get_random_password():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbols = string.punctuation
    all = lower + upper + number + symbols
    temp = random.sample(all, 8)
    password = "".join(temp)
    return password

print(f"A good password example is: {get_random_password()}")

while True:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    password2 = input("Enter the password again: ")
    if password == password2:
        break

categories = {
    "lower": 0,
    "upper": 0,
    "number": 0,
    "symbol": 0,
}

for i in password:
    if str(i) in str(lower):
        categories["lower"] += 1
        continue
    if str(i) in str(upper):
        categories["upper"] += 1
        break
    if str(i) in str(number):
        categories["number"] += 1
        break
    if str(i) in str(symbols):
        categories["symbol"] += 1
        break

print(categories)