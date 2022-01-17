# Asks user for a number that they want the cube root of
num = int(input("What number do you want to find the cube root of ? "))
# Creates a list that is used by the Approximation formulae
litfam = [69]
# Runs 69420 times to ensure accuracy
for x in range(69420):
    # Appends the (1/3)*((2*litfam[x])+(num/(litfam[x]**2)))
    litfam.append((1/3)*((2*litfam[x])+(num/(litfam[x]**2))))
# Prints the cube root
print(litfam[len(litfam)-1])