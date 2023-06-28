def longestConsecutive(nums) -> int:
    x = list(nums) # temporary copy
    x.sort()
    y = 0
    run = []
    for i in range(len(x)):
        run.append(x[i])
        for j in range(len(x)):
            if x[j] == x[i] + 1:
                run.append(x[j])
        y = max([y, len(run)])
        run = []
    print(y)

longestConsecutive([100,4,200,1,3,2])