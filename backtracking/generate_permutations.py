# n = 3
# 0 1 2 
# 0 2 1
# 1 0 2
# 1 2 0
# 2 0 1
# 2 1 0

def generate_permutations(pos: int, n: int, permutation = []):
    if pos == n:
        # if the corresponding queen configuration is valid
        # then count it 
        # to check it, you need to check the diagonals
        print(permutation)
        return 

    for i in range(0, n):
        if i in permutation: # if i is already on the permutation
            continue # we ignore it, 'cause numbers can't repeat on a permutation
           
        # OPTIMIZED PRUNNING
        # EARLY prunning
        # check if putting a queen on the row i on the current column generates a conflict
        # if it does, you can ignore this i
        # and do an early prunning 
         
        permutation.append(i) # insert the number in the permutation
        generate_permutations(pos + 1, n, permutation)
        # we backtrack, and rollback the changes
        permutation.pop() # that removes the i that was recently inserted
        
generate_permutations(0, 3)