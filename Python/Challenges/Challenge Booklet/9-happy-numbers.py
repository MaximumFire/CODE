# Happy Numbers
user_number = input("Enter a number to check if it is happy or not: ")

number_list = []
counter = 0

for i in user_number:
    number_list.append(i)

while True:
    temp_square = 0
    total = 0
    temp_list = []
    counter += 1
    for j in number_list:
        temp_square = int(j) * int(j)
        total += temp_square
    for k in str(total):
        temp_list.append(k)
    number_list = temp_list
    if total == 1:
        print(f"The total is {total}")
        print(f"{user_number} is a happy number!")
        break
    else:
        print(f"The total is {total}")
        print(f"{user_number} is not a happy number!")
        if counter > 50:
            break
        else:
            continue