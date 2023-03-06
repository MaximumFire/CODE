def simplify(num, den):
    if num < 0: x = -num
    else: x = num
    if den < 0: y = -den   
    else: y = den
    if x > y: smaller = y  
    else: smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)): hcf = i
    return (num/hcf, den/hcf)

print(simplify(27, -81))