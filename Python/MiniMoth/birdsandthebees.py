import time as t
from random import *

#declaring variables as usual
minimoth = []
mothcount = int(input("How many minimoths do you want to create "))
start_time = t.time()
foodcount = (mothcount - 2)
foundfood = {}
conflictvalue = []
outcome = 42

#here is where we define our creatures
class MiniMoth:
    def __init__(self, passport, strength = 0, speed = 0, food = 1):
        self.strength = strength
        self.speed = speed
        self.food = food
        self.foundfood = foundfood
        self.passport = passport
    
    #function for creatures to get food
    def getrandomfood(self):
        global foodcount, foundfood
        x = randrange(0, foodcount)
        if str(x) in foundfood:
            if len(foundfood[str(x)]) == 2:
                badamounts = []
                for key in foundfood:
                    if len(foundfood[key]) == 2:
                        badamounts.append(int(key))
                while True:
                    x = randrange(0, foodcount)
                    if x in badamounts:
                        continue
                    else:
                        break
                if str(x) in foundfood:
                    foundfood[str(x)].append(self.passport)
                else:
                    foundfood[str(x)] = [self.passport]
            else:
                foundfood[str(x)].append(self.passport)
        else:
            foundfood[str(x)] = [self.passport]


for i in range(0, mothcount):
    minimoth.append(MiniMoth(i, randrange(0, 25), randrange(0, 25)))


#FOR DEBUGGING



def fightclub(strength1, strength2):
    global outcome
    while True:
        x = (randrange(0,25) + strength1)
        y = (randrange(0,25) + strength2)
        if x > y:
            outcome = 0
            break
        elif y > x:
            outcome = 1
            break

        elif x == y:
            continue
        else:
            print('OK this fucked up')
            break



#here we find food for each minimoth
for i in range(0, mothcount):
    minimoth[i].getrandomfood()

print("food generated")

#make it a list of lists, idk, we'll figure it out eventually
for i in foundfood:
    if len(foundfood[i]) == 2:
        pear = []
        for passport in foundfood[i]:
            for moth in minimoth:
                if moth.passport == passport:
                    pear.append(moth)
        conflictvalue.append(pear)
    else:
        continue
    
print("conflicts made")

for i in range(0, len(conflictvalue)):
    fightclub(conflictvalue[i][0].strength, conflictvalue[i][1].strength)
    if outcome == 0:
        minimoth.remove(conflictvalue[i][1])
        for x in range(len(minimoth)):
            minimoth[x].passport = x
    elif outcome == 1:
        minimoth.remove(conflictvalue[i][0])
        for x in range(len(minimoth)):
            minimoth[x].passport = x
    
print("fights done and deleted dead moths")
               
    


#print(foundfood)
print(len(minimoth))

print("--- %s seconds ---" % (t.time() - start_time))