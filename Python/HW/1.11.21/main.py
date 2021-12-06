noAdults = int(input("How many adult tickets (20): "))
noChildren = int(input("How many child tickets (20): "))
noOap = int(input("How many oap tickets (20): "))

total = (20*noAdults) + (12*noChildren) + (11*noOap)

while True:
    print("Please pay in 10 and 20 pound notes only.")
    print(total)
    payAmount = int(input("How much are you paying?: "))
    if payAmount == 10 or payAmount == 20:
        total = total - payAmount
    else:
        continue
    if total > 0:
        continue
    if total < 0:
        break
    if total == 0:
        break

if total < 0:
    change = (total * -1)
    print("Your change is : " + str(change))

print("Thanks for your purchase.")
    
    
    
          
