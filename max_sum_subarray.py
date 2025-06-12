def solve(n, array):
    best_sum = -(10**12) # -1000_000_000_000
    best_left, best_right = None, None # the left and right endpoints of the best interval (the interval whose sum is best_sum)
    
    # for all [left, right] pairs with left <= right, compute the sum
    for left in range(0, n): # this goes through 0, 1, 2, ..., n - 1
        
        interval_sum = 0
        
        for right in range(left, n): # this goes through left, left+1, left+2, ..., n - 1
            # since right is going in increasing order, that means that we're extending our interval by
            # one position to the right
            interval_sum += array[right]

            if best_sum < interval_sum: # if the best sum so far is worse (less) than the new one, then we update it
                best_sum = interval_sum
                best_left, best_right = left, right # the optimal interval so far becomes the new one 
                
    return best_left, best_right 


def solve_smart(n, array):
    best_sum = -(10**12) # -1000_000_000_000
    best_left, best_right = None, None 
    
    interval_sum = 0
    left = 0
    right = 0
    
    for i in range(0, n):
        right = i 
        interval_sum += array[i]
        if best_sum < interval_sum:
            best_sum = interval_sum
            best_left, best_right = left, right 
            
        if interval_sum < 0:
            interval_sum = 0
            left = i + 1
            
            
    
    return best_left, best_right 

def main():
    # read the input
    n = int(input()) # reading the length of the array (the length is n)
    array = list(map(int, input().split())) # defacto way of reading a list where the elements are space-separated 
    
    best_left, best_right = solve(n, array)
    print(best_left, best_right)
    
if __name__ == "__main__":
    main()
