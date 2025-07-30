from time import time 
from sys import setrecursionlimit, getrecursionlimit, set_int_max_str_digits, get_int_max_str_digits

def factorial(n: int) -> int:
    if n == 0:
        return 1     
    return factorial(n - 1) * n 

# create a decorator that will count the number of times a recursive call is made
# eg: for n = 5 we want for the decorator to compute:
# 5 -> 1 call
# 4 -> 1 call
# 3 -> 2 calls
# 2 -> 3 calls
# 1 -> 5 calls
# 0 -> 3 times 



counter = dict()

def call_counter(func):    
    def wrapper(n: int):
        if n not in counter:
            counter[n] = 0
        counter[n] += 1
        return func(n)
    return wrapper 

# add a new decorator to cache the computed values to not repeat computations
# technique: memoization 
# TODO: after the break 

lookup = dict()

def memoizer(func):
    """
    it caches the returned values so that they're not computed again
    the 2nd time they're requested in the recursion, they're already stored
    so we just look at the stored value and return it 
    """
    def wrapper(n: int) -> int:
        if n in lookup:
            return lookup[n]
        lookup[n] = func(n)
        return lookup[n]
    return wrapper 
    

@call_counter
@memoizer
def fibonacci(n: int) -> int:
    # bases cases
    # the values of n for which we stop the recursion
    if n == 0:
        return 0 
    if n == 1:
        return 1 
    # recursive step
    branch1 = fibonacci(n - 1)
    branch2 = fibonacci(n - 2)
    return branch1 + branch2
    
def power(base: int, exponent: int, modulo) -> int:
    """
    returns (base ** exponent) % modulo
    it doesn't use the ** operator
    """
    if exponent == 0:
        # any number to the 0-th power is 1
        return 1 

    if exponent % 2 == 0:
        power_half_exponent = power(base, exponent // 2, modulo)
        return (power_half_exponent * power_half_exponent) % modulo 
    
    previous_power = power(base, exponent - 1, modulo)
    return (previous_power * base) % modulo


def main():
    
    exponent = 1000_000_000
    base = 2 
    modulo = 3
    
    print(power(base, exponent, modulo))
    
    # starting_time = time()
    # n = 1000_000
    # f = fibonacci(n)
    # end_time = time()
    # print("duration:", end_time - starting_time, "seconds")
    # print(f"computed fibonacci({n}) = {f}")
    # # for n in counter:
    # #     print(f"{n} was called {counter[n]} times")
    
if __name__ == '__main__':
    setrecursionlimit(10**9) # the depth of the recursion is 100M (which is a lot)
    set_int_max_str_digits(50000)
    main()
