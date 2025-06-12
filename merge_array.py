def merge(array1: list[int], array2: list[int]) -> list[int]:
    """
    array1: a list of sorted integers
    array2: a list of sorted integers
    this algorithm merges them in linear time, by using two pointers
    
    result: the merged array (sorted)
    """
    
    n = len(array1)
    m = len(array2)
    
    i = 0
    j = 0
    
    result_array = [None for _ in range(n + m)] # the final array has length n + m 
    
    while i < n and j < m:
        # now we're poiting to array1[i] and array2[j]
        if array1[i] > array2[j]:
            result_array[i+j] = array2[j]
            j += 1
        else:
            result_array[i+j] = array1[i]
            i += 1
    
    while i < n:
        result_array[i+j] = array1[i]
        i += 1
    
    while j < m:
        result_array[i+j] = array2[j]
        j += 1 
        
    return result_array

def main():
    a = [1, 3, 5, 8, 13]
    b = [4, 6, 7, 9, 10, 14, 15]
    c = merge(a, b)
    print(c)
    
if __name__ == '__main__':
    main()
    
        
        