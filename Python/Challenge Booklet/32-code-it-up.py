#Code it up

def encode(x):
    lst = []
    for i in x:
        lst.append(i)
    for j in range(len(lst)):
        lst[j] = ord(lst[j])
        lst[j] = lst[j] + 25
        lst[j] = chr(lst[j])
    string = ""
    for k in lst:
        string = string + k
    return string

print(encode("connor"))