with open("CODE/Python/AdventOfCode/2023/Day 7/input.txt") as f:
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]
    lines = [line.split(" ") for line in lines]

vals = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}

def get_type(hand):
    freq = {}
    for card in hand:
        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1

    for i in range(len(hand)):
        if hand[i] == "J":
            max = 0
            for val in vals:
                if val != "J":
                    newHand = hand[:i] + val + hand[i+1:]
                    if get_type(newHand) > max:
                        max = get_type(newHand)
            return max

    # five of a kind
    if 5 in freq.values():
        return 7
    # four of a kind
    elif 4 in freq.values():
        return 6
    # full house
    elif 3 in freq.values() and 2 in freq.values():
        return 5
    # three of a kind
    elif 3 in freq.values():
        return 4
    # two pair
    elif len(freq.values()) == 3:
        return 3
    # one pair
    elif len(freq.values()) == 4:
        return 2
    # high card
    else:
        return 1
    
def compare_hands(hand1, hand2):
    if get_type(hand1) > get_type(hand2):
        return 1
    elif get_type(hand1) < get_type(hand2):
        return 2
    
    for i in range(len(hand1)):
        if vals[hand1[i][0]] > vals[hand2[i][0]]:
            return 1
        elif vals[hand1[i][0]] < vals[hand2[i][0]]:
            return 2
        
def bubbleSort(arr):
    swapped = False
    n = len(arr)
    for i in range(n-1):
        print("progress: " + str(i) + "/" + str(n))
        for j in range(0, n-i-1):
            if compare_hands(arr[j][0], arr[j+1][0]) == 1:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr

def get_winnings(lines):
    winnings = 0
    sorted = bubbleSort(lines)
    for i in range(len(sorted)):
        winnings += int(sorted[i][1]) * (i+1)
    return winnings

print(get_winnings(lines))