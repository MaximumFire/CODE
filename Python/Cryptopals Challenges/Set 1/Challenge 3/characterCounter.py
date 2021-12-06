frequencies = {}
string = ""

with open("bee.txt", "r") as f:
    string = f.read()
    f.close

for i in string:
    if i == " " or i == "\n":
        continue
    try:
        frequencies[i] += 1
    except:
        frequencies[i] = 1

highest = "a"
highestFrequency = 0


for character in frequencies:
    if frequencies[character] > highestFrequency:
        highest = character
        highestFrequency = frequencies[character]


with open("results.txt", "w") as f:
    f.write(str(frequencies))
    f.close()

print(highest)
print(highestFrequency)