from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    for i in range(int(input("Enter number of iterations: "))):
        print(i, fib(i))

if __name__ == "__main__":
    main()
