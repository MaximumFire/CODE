count = 0
counting = True
i = 1
while True:
    if (len(input())) < i:
        counting = False
    else:
        if counting:
            count += 1
    i += 1

print(count)
