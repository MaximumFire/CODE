import random

with open("ouput.txt", "w") as f:
    outputString = ""
    for i in range(0, 1000000):
        outputString = outputString + str(random.randint(0, 9))
    f.write(outputString)
    f.close()

