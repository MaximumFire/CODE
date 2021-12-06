class Hcf_lcm():
    def __init__(self, numbers):
        self.numbers = numbers
    
    def find_hcf(self):
        x = self.numbers[0]
        y = self.numbers[1]

        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller+1):
            if ((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf

    def find_lcm(self):
        x = self.numbers[0]
        y = self.numbers[1]
        if x > y:
            greater = x
            smaller = y
        else:
            greater = y
            smaller = x

        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += smaller
        return lcm
    
    def prime_factors(self):
        i = 2
        n=self.numbers[0]
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors