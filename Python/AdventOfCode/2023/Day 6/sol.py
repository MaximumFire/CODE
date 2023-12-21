with open("CODE/Python/AdventOfCode/2023/Day 6/input.txt", "r") as f:
    times = [int(x) for x in f.readline()[5:].strip("\n").split(" ") if x != ""]
    print(times)
    
    distances = [int(x) for x in f.readline()[9:].strip("\n").split(" ") if x != ""]
    print(distances)

# Part 1
def get_distance(time_held, time_allowed):
    # d = v * t
    # time_held is equal to the velocity of the boat
    return time_held * time_allowed

def part1(times, distances):
    result = 1

    for i in range(len(times)):
        ways_to_win = 0
        for j in range(times[i]):
            time_held = j
            time_allowed = times[i] - j
            distance = get_distance(time_held, time_allowed)
            if distance > distances[i]:
                ways_to_win += 1
        result *= ways_to_win

    return result

# Part 2
def part2(times, distances):
    time = int("".join([str(x) for x in times]))
    distance = int("".join([str(x) for x in distances]))
    result = 0

    for i in range(time):
        time_held = i
        time_allowed = time - i
        if get_distance(time_held, time_allowed) > distance:
            result += 1

    return result

print(part1(times, distances))
print(part2(times, distances))