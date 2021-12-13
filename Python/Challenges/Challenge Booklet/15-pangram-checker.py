#Pangram Checker
used_letters = []
user_string = input("Enter a string to be checked: ").lower()
string_list = []
for j in user_string:
    if j != " ":
        string_list.append(j)
for i in string_list:
    if i not in used_letters:
        used_letters.append(i)
if len(used_letters) == 26:
    pangram = True
else:
    pangram = False
print(pangram)