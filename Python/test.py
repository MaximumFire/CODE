# write a function to do the bubble sort

def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

print(bubble_sort([1,3,2,5,4,7,6,9,8]))