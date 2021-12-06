import itertools as it # Imports the iteration tools package
numbers = [] # Defines a list that the 4 numbers will be put inside of.
for i in range(0, 4): # Loop that adds the numbers to the list.
    temp = int(input(f"Enter a number ({i+1} out of 4): ")) # Gets a number from the user
    numbers.append(temp) # Add the number to the list
final = list(it.permutations(numbers, 4)) # Creates a variable to hold the permutations of the numbers in lengths of 4
for j in final: # Loop that prints out the different combinations on seperate lines
    print(j) # Prints the current combination.