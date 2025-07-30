import functools

arr = [5, 6, 2, 3, -2, 4, 10, 0]
cache = dict()
def memoizer(func):
    @functools.wraps(func)
    def wrapper(*args) -> int:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

previous = [None for _ in range(len(arr))]

@memoizer
def longest_increasing_subsequence(n: int) -> int:
    
    result = 1
    for i in range(n):
        if arr[i] < arr[n]:
            tmp_lis = longest_increasing_subsequence(i) + 1
            if result < tmp_lis:
                result = tmp_lis
                previous[n] = i 
    return result 

def main():
    
    n = 0
    for i in range(len(arr)):
        if longest_increasing_subsequence(i) > longest_increasing_subsequence(n):
            n = i 
        
    # after that loop, n is the best position to end the LIS
    
    subsequence = []
    while n is not None:
        subsequence.append(n)
        n = previous[n]

    subsequence = subsequence[::-1]
    print("indices:", subsequence)
    print("values:", [arr[i] for i in subsequence])
    

if __name__ == '__main__':
    main()