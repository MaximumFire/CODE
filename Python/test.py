x = int(input())
y = int(input())

out = ""

z = (x/100) + y
w = x + (y/100)

if z < 20:
    out += f"£{z}\n"
if w < 20:
    out += f"£{w}"

print(out)