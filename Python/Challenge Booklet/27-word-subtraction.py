#Word Subtraction

def main(x, y):
    xtotal = 0
    ytotal = 0
    for i in range(len(x)):
        xtotal += ord(x[i])
    for j in range(len(y)):
        ytotal += ord(y[j])
    print(xtotal-ytotal)

main("connor", "maive")