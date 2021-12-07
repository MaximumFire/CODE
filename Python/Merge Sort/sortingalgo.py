import random
from heapq import merge

def merge_custom(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])

    return result


def merge_sort(m):
    if len(m) <= 1:
        return m
    
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge_custom(left, right))


def get_random_list(length):
    lst = []
    for i in range(length):
        lst.append(random.randrange(0, length*10))
    return lst


lst = get_random_list(10)
print(lst)
print("Sorting...")
print(merge_sort(lst))