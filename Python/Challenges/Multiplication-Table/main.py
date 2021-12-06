userinput1 = int(input("Enter the starting number for the multiplication table: "))
userinput2 = int(input("Enter the ending number for the multiplication table: "))
max_length = len(str((userinput2-1)*(userinput2-1)))
for i in range(userinput1, userinput2): 
    for j in range(userinput1, userinput2):
        if j == (userinput2 - 1): 
            slot = j * i
            if len(str(slot)) < max_length: 
                for k in range(len(str(slot)), max_length):
                    slot = "0" + str(slot)
            print(slot)
        else: 
            slot = j * i
            if len(str(slot)) < max_length: 
                for k in range(len(str(slot)), max_length):
                    slot = "0" + str(slot)
            print(slot, end=' ')