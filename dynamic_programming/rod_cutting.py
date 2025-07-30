import random 
import functools
import sys 

N = 10000
price = [random.randint(1, 10) for _ in range(N+1)]
optimal = [None for _ in range(N+1)]
counter_calls = dict()
cache = dict()

def profiler(func):
    @functools.wraps(func)
    def wrapper(n: int) -> int:
        if n not in counter_calls:
            counter_calls[n] = 0
        counter_calls[n] += 1
        return func(n)
    return wrapper 

def memoizer(func):
    @functools.wraps(func)
    def wrapper(n: int) -> int:
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@profiler
@memoizer
def max_revenue(n: int) -> int:
    if n == 0:
        return 0
    result = None 
    for i in range(1, n + 1):
        tmp_revenue = price[i] + max_revenue(n - i)
        if result is None or result < tmp_revenue:
            result = tmp_revenue
            optimal[n] = i
    return result 



def main():
    print(max_revenue(N))
    
    # BOTTOM-UP approach
    max_rev = [None for _ in range(N + 1)]  
    # base cases first
    # then go through all states in increasing order of computation
    # apply the transition rules
    max_rev[0] = 0
    for n in range(1, N + 1):  # we go in increasing order because f(n) depends on f(numbers less than n)
        for i in range(1, n + 1):
            max_rev[n] = max(max_rev[n - i] + price[i], max_rev[n])
    
    # for n in counter_calls:
    #     print(n, '-->', counter_calls[n])
    

if __name__ == '__main__':
    sys.setrecursionlimit(10**8)
    main()