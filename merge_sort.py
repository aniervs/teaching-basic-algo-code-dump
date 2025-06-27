from time import time 

def merge(a: list, b: list) -> list:
    """
    this receives two sorted arrays
    and returns a sorted array that contains all the elements from both
    time complexity: O(|a| + |b|)
    """
    c = []
    n, m = len(a), len(b)
    i, j = 0, 0 
    while i < n and j < m:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1 
        else:
            c.append(b[j])
            j += 1
    while i < n:
        c.append(a[i])
        i += 1
    while j < m:
        c.append(b[j])
        j += 1         
    
    return c 

def merge_sort(array: list) -> list:
    n = len(array)
    if n == 1:
        return array
    left = array[ : n//2]
    right = array[n//2 :]
    left = merge_sort(left) # the recursive step on the left half (divide phase)
    right = merge_sort(right) # the recursive step on the right half (divide phase)
    # now comes the conquer step
    return merge(left, right) # merging two sorted arrays

def main():
    n = 10**6
    arr = list(range(n, 0, -1)) # a decreasing array of length n -> [n, n - 1, n - 2, ..., 1]
    starting_time = time()
    merge_sort(arr)
    ending_time = time()
    print(f"elapsed time: {ending_time - starting_time} seconds")

if __name__ == '__main__':
    main()