from random import randint 
from hello import solve, solve_smart
from time import time 
from tqdm import tqdm 

n = 5000
for _ in tqdm(range(100)):
    array = [
        randint(-10, 10) for _ in range(n)
    ]
    
    brute_solution = solve(n, array) # old O(n^2) solution
    smart_solution = solve_smart(n, array) # smart O(n) solution 

    if brute_solution != smart_solution:
        print("OOPS! Something is wrong")
        print("input:", array)
        print("smart output:", smart_solution)
        print("brute output:", brute_solution)
        
        exit(-1)
    
print("All correct!")
    
