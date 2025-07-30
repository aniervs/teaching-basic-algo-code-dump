def binary_search(left, right, array, target):
    """
    this finds the first position p on the interval [left, right] 
    where array[p] >= target (lower_bound)
    """
    
    if left == right - 1:
        # two numbers 
        # either left or right is the final position
        if array[left] < target:
            return right 
        return left 
        
    
    mid = (left + right) // 2
    if array[mid] >= target:
        # then, the final position should be mid or possibly something to its left
        return binary_search(left, mid, array, target)
    # otherwise, we have array[mid] < target
    return binary_search(mid, right, array, target)
    