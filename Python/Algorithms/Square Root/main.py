# Asks user for a number that they want the square root of
num = int(input("What number do you want to find the square root of ? "))
# Creates a list that is used by the Approximation formulae
litfam = [69]
# Runs 69420 times to ensure accuracy
for x in range(69420):
    # Appends the 0.5*(litfam[x]+(num/litfam[x]))
    litfam.append(0.5*(litfam[x]+(num/litfam[x])))
# Prints the Square root
print(litfam[len(litfam)-1])