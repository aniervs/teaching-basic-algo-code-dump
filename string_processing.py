MOD = 10**9 + 7 # this is a prime number
BASE = 311 # also prime. I choose it because it's greater than 255 (so it covers all ASCII) characters
# precomputing the powers of the BASE 
POWERS_BASE = [1 for _ in range(10**6)]
for i in range(1, 10**6):
    POWERS_BASE[i] = (POWERS_BASE[i - 1] * BASE) % MOD # B**i = (B**(i - 1)) * B

def pattern_matching(text: str, pattern: str) -> list[int]:
    """
    it finds all the positions i such that text[i:i+len(pattern)] == pattern
    """
    
    matches = []
    
    n, m = len(text), len(pattern)
    
    hash_pattern = 0
    for i in range(m):
        # print(pattern[i], '-->', ord(pattern[i]))
        hash_pattern = (hash_pattern * BASE + ord(pattern[i])) % MOD 
    
    hash_window = 0
    for i in range(m):
        hash_window = (hash_window * BASE + ord(text[i])) % MOD 
        
    for i in range(0, n - m + 1):
        if hash_pattern == hash_window:
            # found a match 
            matches.append(i)
        hash_window = (hash_window - (ord(text[i]) * POWERS_BASE[m - 1]) % MOD + MOD) % MOD # removed text[i]
        if i + m < n:
            hash_window = (hash_window * BASE + ord(text[i + m])) % MOD # appending text[i + m]
            
    return matches 

def main():
    text = input()
    pattern = input()
    print(pattern_matching(text, pattern))
    
if __name__ == '__main__':
    main()
    