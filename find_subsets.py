# backtracking (the step of "rolling back" the changes when going up on the tree is called "backtrack")

def find_subsets(pos: int, n: int, subset: set = set()):
    if pos == n:
        print(list(subset))
        return 
    find_subsets(pos + 1, n, subset)
    subset.add(pos)
    find_subsets(pos + 1, n, subset)
    subset.remove(pos)

def generate_binary_sequences(pos: int, n: int, string: str = ""):
    print(f"pos: {pos}, n: {n}, string: {string}")
    if pos == n:
        print(string)
        return 
    generate_binary_sequences(pos + 1, n, string + "0")
    generate_binary_sequences(pos + 1, n, string + "1")
    

def generate_ternary_sequences(pos: int, n: int, string: str = ""):
    if pos == n:
        print(string)
        return 
    generate_ternary_sequences(pos + 1, n, string + "0")
    generate_ternary_sequences(pos + 1, n, string + "1")
    generate_ternary_sequences(pos + 1, n, string + "2")
    
def generate_k_ary_sequences(pos: int, n: int, k: int, string: str = ""):
    if pos == n:
        print(string)
        return 
    for i in range(0, k):
        generate_k_ary_sequences(pos + 1, n, k, string + str(i))

generate_k_ary_sequences(0, 3, 4)