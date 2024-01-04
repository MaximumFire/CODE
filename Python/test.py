a = "the quick brown fox jumped over the lazy dog"
n = 3

b = []
c = ""

spaces_since_split = 0

for i in range(len(a)):
    if a[i] == " ":
        spaces_since_split += 1
        c += a[i]
    else:
        c += a[i]
    if spaces_since_split == n:
        b.append(c)
        spaces_since_split = 0
        c = ""
    if i == len(a) - 1:
        b.append(c)

print(b)