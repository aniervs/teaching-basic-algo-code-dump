least_factor = []

def sieve(n: int):
    """
    returns least_factor[]: n -> the least prime factor of n
    """    
    global least_factor
    least_factor = [i for i in range(n + 1)] # assume that every number is prime, so initially the least factor of each number is itself
    for i in range(2, n + 1):
        if least_factor[i] == i: # if i is prime
            for j in range(i * i, n + 1, i): # go through the multiples of i
                if least_factor[j] == j: # if j is still being considered prime, which meanst that it hasn't been cross-out in the sieving
                    least_factor[j] = i  # process, then we mark it as not prime, and set i as its least factor



def factorize(n: int) -> list:
    """
    returns the list of prime factors of n 
    it accounts for different multiplicities (prime factors repeating)
    n = 60 -> [ (2, 2), (3, 1), (5, 1) ]
    n = 14700 -> [(2, 2), (3, 1), (5, 2), (7, 2)]
    """
    
    factors = []
    while n != 1:
        p = least_factor[n]
        cnt = 0
        while n % p == 0:
            n = n // p 
            cnt += 1
        # p: a prime factor
        # cnt: the number of times it divides n, aka: the multiplicity of p
        
        factors.append((p, cnt)) # append the tuple of the prime and its multiplicity
    
    return factors

def generate_divisors(factors: list[tuple], pos: int, divisor: int):
    if pos == len(factors):
        print(divisor, end  = ' ')
        return 
    
    prime, exponent = factors[pos]
    prime_power = 1 # starts at prime ** 0 and goes multiplying by the prime each time
    for _ in range(exponent + 1):
        generate_divisors(factors, pos + 1, divisor * prime_power)
        prime_power *= prime  

def sum_divisors(n: int) -> int:
    """ it uses the factorization of n"""
    factors = factorize(n)
    result = 1
    
    for prime, exponent in factors:
        result *= ((prime ** (exponent + 1) - 1) // (prime - 1))

    return result 

def phi(n: int) -> int:
    """
    computes the Euler Function for n
    ie: the amount of numbers less than n that don't have common factors with n 
    """
    factors = factorize(n)
    result = n
    for prime, exponent in factors:
        result *= (prime - 1)
        result //= prime 
    return result 

def main():
    sieve(10_000_000) # compute the least factor of every number from 1 to 10^7
    while True:
        n = int(input())
        print(phi(n))
        print()

if __name__ == '__main__':
    main()

# 60 -> 30 -> 15 -> 5 -> 1
#    2     2     3    5
# 2 * 2 * 2 * 3 * 5 == 60
