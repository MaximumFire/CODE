# find fibonacci numbers from 0 to n

from functools import cache

#@cache
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# get fib(100)
print(fib(100))