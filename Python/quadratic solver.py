def simplify(num, den):
    if num < 0: x = -num
    else: x = num
    if den < 0: y = -den   
    else: y = den
    if x > y: smaller = y  
    else: smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)): hcf = i
    return (num//hcf, den//hcf)

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))


x = int((-1*b)+((b**2)+(-4*a*c))**0.5)
y = int(2*a)
answer1 = ((-1*b)+((b**2)+(-4*a*c))**0.5)/(2*a)
z = int((-1*b)-((b**2)+(-4*a*c))**0.5)
answer2 = ((-1*b)-((b**2)+(-4*a*c))**0.5)/(2*a)

print("-------------------------------------------------")

frac1 = simplify(x, y)
frac2 = simplify(z, y)

print("[decimal] || [fraction]")

if answer1 % 1 == 0:
    print(f"{answer1}")
else:
    print(f"{answer1} || {frac1[0]}/{frac1[1]}")

if answer2 % 1 == 0:
    print(f"{answer2}")
else:
    print(f"{answer2} || {frac2[0]}/{frac2[1]}")