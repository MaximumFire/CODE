def mergeTwoLists(list1, list2):
    final = []
    left1 = 0
    left2 = 0
    list1Done = False
    list2Done = False
    for i in range(0, (len(list1) + len(list2))):
        if left1 > len(list1) - 1:
            list1Done = True
        elif left2 > len(list2) - 1:
            list2Done = True
        if (not list1Done) and (not list2Done): 
            if list1[left1] <= list2[left2]:
                final.append(list1[left1])
                left1 += 1
            else:
                final.append(list2[left2])
                left2 += 1
        elif (not list1Done) and list2Done:
            for j in range(left1, len(list1)):
                final.append(list1[left1])
                left1 += 1
            list1Done = True
        elif (not list2Done) and list1Done:
            for j in range(left2, len(list2)):
                final.append(list2[left2])
                left2 += 1
            list2Done = True

    return final

list1 = [1,2,4]
list2 = [1,3,4]
print(mergeTwoLists(list1=list1, list2=list2))