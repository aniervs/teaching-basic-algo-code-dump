import random 
from tqdm import tqdm 

def insertion_sort(array: list[int]) -> None:
    """
    in-place implementation of sorting
    in-place means that it modifies the input array
    instead of returning a new one
    """
    
    n = len(array)
    for i in range(0, n):
        j = i
        while j - 1 >= 0 and array[j - 1] > array[j]:
            # swap a[j] and a[j - 1]
            array[j], array[j - 1] = array[j - 1], array[j]
            j = j - 1 

def selection_sort(array: list[int]) -> None:
    """
    in-place implemenation of selection sort    
    """
    
    n = len(array)
    for i in range(n): # n iters
        # find the min element in the interval [i, n)
        idx_min = i
        for j in range(i, n): # n - i iters 
            if array[idx_min] > array[j]:
                idx_min = j 
                
        # swap i and the min
        array[i], array[idx_min] = array[idx_min], array[i]
        
def bubble_sort(array: list[int]) -> None:
    """
    in-place bubble-sort 
    """
    
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
def count_sort(array: list[int]) -> None:
    """
    in-place counting sort
    """
    
    n = len(array)
    
    # first step: constructing the frequency array
    # what's the size of such array? answer: max(array) + 1
    
    max_element = max(array) # this iterates through the array and finds the max, hence it takes O(n) time
    count = [0 for _ in range(max_element + 1)] # this takes O(max element) time and memory
    for i in range(n):
        count[array[i]] += 1 
        
    # second step:
    # go through the values (positions in the frequency array)
    # for each x, add as many of x to the final array as count[x]
    
    last_position = 0
    for value in range(0, max_element + 1): # O(max element) in total
        for _ in range(count[value]): # O(freq of the value), thus O(n) in total
            array[last_position] = value 
            last_position += 1 
        
    
    
    
    

def stress():
    for _ in tqdm(range(10000)):
        n = 100
        arr = [
            random.randint(-10, 10) for _ in range(n)
        ]
        sorted_arr = sorted(arr) # this is the built-in sorting method in Python
        # insertion_sort(arr) # this is our sorting function (insertion sort)
        # selection_sort(arr) # this is our sorting function (selection sort)
        bubble_sort(arr)
        if arr != sorted_arr:
            print(f"{arr} is not the expected sorted array")
            print(f"expected sorted array: {sorted_arr}")
            raise AssertionError("Wrong sorting!")
        
        
    print("All tests passed! Congrats.")
            

stress()