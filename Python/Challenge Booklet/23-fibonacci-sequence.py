#Fibonacci sequence calculator

def get_sequence(num_of_places):
    sequence = [0, 1]
    for i in range(num_of_places):
        current = sequence[i] + sequence[i+1]
        sequence.append(current)
    return sequence

def reverse(list):
    new_list = []
    for i in reversed(list):
        new_list.append(i)
    return new_list

def add_up(list):
    total = 0
    for i in list:
        total += int(i)
    return total

a = get_sequence(int(input("Enter number of places to generate: ")))
print(a)
b = reverse(a)
print(f"The reverse of that sequence is: {b}")
total = add_up(a)
print(f"The total of these digits is: {total}")