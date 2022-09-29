from random import * 

sorts = 1
llist = randint(2, 10)
list = []
for i in range(llist):
    list.append(randint(0,100))
# Prints the list to see the difference from beggining to end
# Comments if you don't want to see the start
print(list)
# Creates functionn for sorting a single pair
def sortPair(x):
    global sorts
    # Creates a backup of list[x]
    y = list[x]
    # Checks if no change is needed
    if list[x] <= list[x+1]:
        # Prints the progress of the sort
        # comment if you don't want to see it
        print(list)
    # Checks if a change is needed
    else:
        # Replaces list[x] with the item in front
        list[x] = list[x+1]
        # Replaces list[x+1] with our backup of list[x] because list[x] has changed
        list[x+1] = y
        # Adds to the sort counter
        sorts += 1
        # Prints the progress of the sort
        # comment if you don't want to see it 
        print(list)

# Repeats while changes have been made
# Because if no changes are made in a pass the list is sorted
while sorts != 0:
    # Makes sorts 0 for that pass
    sorts = 0
    # Repeats for the length of the list
    for i in range(len(list)-1):
        # Runs the Pair Sort algorithm
        sortPair(i)