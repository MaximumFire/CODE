import time
def primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for p in range(2, n):
        if prime[p]:
            c += 1
            print(p)
    return c

t0 = time.time()
c = primes(1000000)
print("Total primes in range: " , c)
t1 = time.time()
print("Time required: ", t1-t0)