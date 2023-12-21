with open("CODE/Python/AdventOfCode/2023/Day 9/in.txt") as f:
    data = [line.strip("\n").split(" ") for line in f.readlines()]
    lines = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            temp.append(int(data[i][j]))
        lines.append(temp)

def get_differences(line):
    differences = []
    for i in range(len(line)-1):
        differences.append(line[i+1]-line[i])
    return differences

def all_zeros(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            return False
    return True

def get_next_term(sequence, difference_sequence):
    prev_term = sequence[-1]
    if all_zeros(difference_sequence):
        return prev_term
    return prev_term + get_next_term(difference_sequence, get_differences(difference_sequence))

def get_prev_term(sequence, difference_sequence):
    next_term = sequence[0]
    if all_zeros(difference_sequence):
        return next_term
    return next_term - get_prev_term(difference_sequence, get_differences(difference_sequence))

total_next = 0
total_prev = 0
for i in range(len(lines)):
    total_next += get_next_term(lines[i], get_differences(lines[i]))
    total_prev += get_prev_term(lines[i], get_differences(lines[i]))

print(total_next)
print(total_prev)