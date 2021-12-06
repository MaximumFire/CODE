from random import *
import time as t

#declaring variables as usual
minimoths = []
mothcount = int(input("How many minimothsssss do you want to create "))
foodcount = (mothcount - 2)
foundfood = {}
roundCount = 0
actualRoundCount = 0

#here is where we define our creatures
class MiniMoth:
    def __init__(self, passport, strength = 0, food = 1):
        self.strength = strength
        self.food = food
        self.foundfood = foundfood
        self.passport = passport

    def getrandomfood(self):
        global foodcount, foundfood
        x = randrange(0, foodcount)
        if str(x) in foundfood:
            if len(foundfood[str(x)]) == 2:
                bad_amounts = []
                for key in foundfood:
                    if len(foundfood[key]) == 2:
                        bad_amounts.append(int(key))
                while True:
                    x = randrange(0, foodcount)
                    if x in bad_amounts:
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

def battle(fighters):
    temp = 0
    if fighters[0].strength > fighters[1].strength:
        temp += (fighters[0].strength - fighters[1].strength)
    elif fighters[1].strength > fighters[0].strength:
        temp -= (fighters[1].strength - fighters[0].strength)
    
    mid = 50 + temp
    random_winner = randrange(1, 101)
    if random_winner > mid:
        return 0
    elif random_winner < mid:
        return 1
    else:
        tiebreaker = randrange(0, 2)
        return tiebreaker

def reproduce():
    global minimoths
    for moth in minimoths:
        if moth.food >= 2:
            minimoths.append(MiniMoth(len(minimoths) + 1, randrange(0, 25)))
            moth.food -= 2

    

def main():
    global roundCount, mothcount, foundfood, foodcount, actualRoundCount
    for i in range(0, mothcount):
        minimoths.append(MiniMoth(i, randrange(0, 25)))

    #FOR DEBUGGING
    #for i in range(0, mothcount):
    #    print(str(minimothsssss[i].strength) + ' ' + str(minimothsssss[i].speed))

    for r in range(0, 100):
        #t.sleep(0.1)

        print(f"round count : {actualRoundCount}")

        reproduce()

        if roundCount == 2:
            for minimoth in minimoths:
                minimoth.food -= 1
                if minimoth.food == 0:
                    minimoths.remove(minimoth)
            roundCount = 0

        mothcount = len(minimoths)
        foodcount = (mothcount - 2)

        #here we find food for each minimothssss
        foundfood = {}
        for i in range(0, mothcount):
            minimoths[i].getrandomfood()

        print(f"mothCount: {len(minimoths)}")
        print(f"foundFood: {len(foundfood)}")

        doubles = []
        singles = []
        for food in foundfood:
            if len(foundfood[food]) == 2:
                doubles.append(food)
            elif len(foundfood[food]) == 1:
                singles.append(food)
        print(f"doubles: {len(doubles)}")
        print(f"singles: {len(singles)}")


        winners = []
        losers = []
        fight = []
        for double in doubles:
            fight = []
            for minimoth in minimoths:
                if minimoth.passport in foundfood[double]:
                    fight.append(minimoth)
            winner = battle(fight)
            winners.append(fight[winner])
            if winner == 0:
                losers.append(fight[1])
            elif winner == 1:
                losers.append(fight[0])
        for single in singles:
            for minimoth in minimoths:
                if minimoth.passport in foundfood[single]:
                    winners.append(minimoth)
        for winner in winners:
            winner.food += 1
        print(f"winners : {len(winners)}")
        for loser in losers:
            loser.food -= 1
        print(f"losers : {len(losers)}")

        roundCount += 1
        actualRoundCount += 1
        print("\n")

if __name__ == "__main__":
    main()