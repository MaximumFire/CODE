#Ordering

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # sorting by using simultaneous assignment in python
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = []

choice = input("Integers (a) or Letters (b)?: ")

if choice == "a":
    for i in range(0, 10):
        numbers.append(int(input("Enter a number: ")))
else:
    for i in range(0, 10):
        numbers.append(input("Enter a letter: "))

bubble_sort(numbers)

choice = input("Ascending (a) or descending (d)?: ")

if choice == "a":
    print(numbers)
else:
    numbers.reverse()
    print(numbers)