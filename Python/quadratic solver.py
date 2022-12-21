
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

answer1 = ((-1*b)+((b**2)+(-4*a*c))**0.5)/(2*a)
answer2 = ((-1*b)-((b**2)+(-4*a*c))**0.5)/(2*a)

print(f"{answer1}, {answer2}")