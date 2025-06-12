def solve(n: int, array: list[int], q: int, queries: list[tuple[int,int]]) -> list[int]:
    
    result = [] # contains the sums of each of the intervals asked (those in the queries list)
    for l, r in queries:
        interval_sum = 0
        for i in range(l, r): # l, l+1, ..., r - 1
            interval_sum += array[i]
        result.append(interval_sum)
    return result         

def solve_smart(n: int, array: list[int], q: int, queries: list[tuple[int,int]]) -> list[int]:
    
    partial_sums = [0] * (n + 1) # [0, 0, 0, ..., 0]
    for i in range(0, n):
        partial_sums[i + 1] = partial_sums[i] + array[i]
        
    results = []
    for l, r in queries: # each query consists of (l, r): the bounds of the interval
        answer = partial_sums[r] - partial_sums[l]
        results.append(answer)
    
    return results 

    

def main():
    N, Q = map(int, input().split())
    
    array = list(map(int, input().split()))
    
    queries = []
    for _ in range(Q): # do it Q times 
        l, r = map(int, input().split()) # read the bounds of an interval
        queries.append((l, r)) # append that interval into the list of queries
        
    # answers = solve(N, array, Q, queries)
    answers = solve_smart(N, array, Q, queries) # the solution with partial sums 
    for ans in answers:
        print(ans)
    # print(*answer, sep = '\n')
    
        
if __name__ == '__main__':
    main()