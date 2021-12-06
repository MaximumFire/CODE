#Palindrome checker

def check(string):
    if string == string[::-1]:
        return True
    else:
        return False

string  = input("Enter a string to check if it is a palindrome: ")
isPalindrome = check(string)
print(f"Status of check: {isPalindrome}")