words = [None, 'abc', 'ab', 'cd', 'abcde'] # indexing words from 1
L = 5

optimal = [None for _ in range(len(words))]

def cost_split(j: int, i: int):
    """
    splitting 1, 2, ..., j, j+1, ..., i into
    1, 2, ..., j    j+1,j+2,...,i
    """
    
    cost = L
    for k in range(j + 1, i + 1):
        cost -= len(words[k])
    return cost ** 3

def is_valid(j: int, i: int) -> bool:
    """
    it checks that
        len(words[j+1]) + len(words[j+2]) + ... + len(words[i]) <= L
    """
    sum_lengths = 0
    for k in range(j + 1, i + 1):
        sum_lengths += len(words[k])
    return sum_lengths <= L # true if sum <= L, otherwise false

def min_cost_split(i: int) -> int:
    """
    returns the optimal cost of splitting the words from 1st to i-th
    """
    if i == 0:
        return 0
    result = float("inf")
    for j in range(0, i): # j < i
        if is_valid(j, i):
            tmp_cost = min_cost_split(j) + cost_split(j, i)
            if result > tmp_cost:
                result = tmp_cost
                optimal[i] = j 
    return result 
    

def main():
    for i in range(0, 5):
        print(min_cost_split(i), end = ' ')
    print()
    
    lines = []
    n = 4
    while n != 0:
        k = optimal[n]
        lines.append(words[k + 1:n+1])
        # take the words from optimal[n]+1 till n 
        # and put them in a line 
        n = k 
        
    lines = lines[::-1]
    for line in lines:
        print(line)


if __name__ == '__main__':
    main()