import threading
import random as r
from time import sleep as s

time = 0
active = True

def timer():
    global time
    while active:
        s(1)
        time += 1

def main():
    while True:
        IsMultiplication = r.randint(1, 3)
        if IsMultiplication == 1:
            num1 = r.randint(10, 100)
            num2 = r.randint(10, 100)
            if ((num1 * num2) % 1) == 0:
                return num1, "*", num2, (num1 * num2)
            else:
                continue
        else:
            num1 = r.randint(10, 100)
            num2 = r.randint(10, 100)
            if ((num1 / num2) % 1) == 0:
                return num1, "/", num2, (num1 / num2)
            else:
                continue
                
timer = threading.Thread(target=timer)
timer.start()

num_correct = 0

for i in range(10):
    nums = main()
    print(f"What is {nums[0]} {nums[1]} {nums[2]}?")
    print(nums[3])
    answer = int(input("Your answer: "))
    if answer == nums[3]:
        print("Well done, that is correct.")
        num_correct += 1
    else:
        print("That is incorrect.")

active = False
print(f"That took you {time} seconds.")