def average(nums):
    total = 0
    count = 0
    for i in nums:
        total += i
        count += 1
    average = (total / count)
    return average

nums = []

while True:
    number = int(input("Enter a number: "))
    nums.append(number)
    choice = input("Calculate (c) or go again (): ")
    if choice == "c":
        print(average(nums))
        break

