from dynamic_programming.lis import memoizer

a = "abcdt"
b = "aczdw"
optimal = [
    [None for _ in range(len(b) + 1)]
    for _ in range(len(a) + 1)
] # (len(a) + 1) * (len(b) + 1) array

@memoizer
def longest_common_subsequence(n, m):
    if n == 0 or m == 0:
        return 0 
    
    if a[n - 1] == b[m - 1]:
        optimal[n][m] = "match" # (n,m) -> (n-1, m-1)
        return 1 + longest_common_subsequence(n - 1, m - 1)
    
    # a[n - 1] != b[m - 1]
    option1 = longest_common_subsequence(n-1, m)
    option2 = longest_common_subsequence(n, m - 1)
    if option1 < option2:
        optimal[n][m] = "option2"
        return option2
    else:
        optimal[n][m] = "option1"
        return option1

def main():
    l = longest_common_subsequence(len(a), len(b))
    n, m = len(a), len(b)
    
    matches = []
    
    while n != 0 and m != 0:
        choice = optimal[n][m]
        if choice == "match":
            matches.append( (n - 1, m - 1) )
            n -= 1
            m -= 1
        elif choice == "option1":
            n -= 1
        elif choice == "option2":
            m -= 1  
        else:
            raise AssertionError("invalid choice")
        
    matches = matches[::-1]
    
    print("a:", a)
    print("b:", b)
    print("length of the LCS:", l)
    for (i, j) in matches:
        print(i, j, '->', a[i])
    

if __name__ == '__main__':
    main()