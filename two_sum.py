from copy import copy 

def two_sum(array, target):
    """
    array: the input array
    target: the goal number
    """
    
    array.sort() # assume this is fast: O(n log n) -> merge sort + quick sort 
    
    n = len(array)
    
    i = 0
    j = n - 1 
    while i < j:
        while i < j and array[i] + array[j] > target:
            j -= 1 
            
        # now array[i] + array[j] <= target, so we just need to check if they add up to target exactly
        if i < j and array[i] + array[j] == target:
            return array[i], array[j] # returning the values 
        i += 1
    
    return None, None 

def main():
    n, x = map(int, input().split())
    arr =  list(map(int, input().split()))
    
    # HINT FOR AN IDEA to recover the original positions
    # instead of storing a0, a1, a2, ...
    # you can store (a0, 0), (a1, 1), (a2, 2), (a3, 3), ...
    # when sorted, this lists compares the a_i values 
    # so you can run the standard 2-sum algorithm with the first item of each tuple
    # once you find two positions i, j, you can recover the original positions by looking at their second item 
    
    i, j = two_sum(array=copy(arr), target=x)
    if i is None:
        print("IMPOSSIBLE")
    else:
        pos_i = arr.index(i)
        pos_j = arr.index(j)
        if pos_j == pos_i: # it found the same position
            pos_j = arr.index(j, pos_i + 1)
        print(pos_i + 1, pos_j + 1)
    
    
if __name__ == '__main__':
    main()