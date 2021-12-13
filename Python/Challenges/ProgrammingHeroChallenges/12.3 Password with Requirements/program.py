import string
import random

def generate_password(size: int):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(size - 4):
        password += random.choice(all_chars)
    
    return password

size = int(input("Please enter password length : "))
print(f"First Random Password is : {generate_password(size)}")
print(f"Second Random Password is : {generate_password(size)}")
print(f"Third Random Password is : {generate_password(size)}")