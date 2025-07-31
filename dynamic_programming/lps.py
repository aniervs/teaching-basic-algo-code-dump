from dynamic_programming.lis import memoizer

s = "dantwxwnac"

optimal = [[None for _ in range(len(s))] for _ in range(len(s))] # len(s) x len(s)
# -> optimal[l][r]: the optimal choice between
# 1. matching (s[l], s[r])
# 2. ignoring s[l]
# 3. ignoring s[r]

@memoizer
def longest_palindrome_substring(left: int, right: int) -> int:
    if left == right: # a one-letter interval
        optimal[left][right] = "match"
        return 1 # it's always palindrome
    
    if left == right - 1: # a two-letter interval
        if s[left] == s[right]:
            optimal[left][right] = "match"
            return 2
        optimal[left][right] = "left" # go left -> ignore s[right]
        return 1 

    # right - left > 1 (at least three characters)
    if s[left] == s[right]:
        optimal[left][right] = "match"
        return 2 + longest_palindrome_substring(left + 1, right - 1)
    option1 = longest_palindrome_substring(left, right - 1)
    option2 = longest_palindrome_substring(left + 1, right)

    if option1 > option2: 
        optimal[left][right] = "left"
        return option1
    optimal[left][right] = "right"
    return option2

def main():
    global s
    s = input() # "dantwxwnac"
    lps = longest_palindrome_substring(0, len(s) - 1)
    print(lps)
    left = 0
    right = len(s) - 1    

    left_endpoints = []
    right_endpoints = []

    while left <= right:
        choice = optimal[left][right]
        if choice == "match":
            left_endpoints.append(left)
            if left != right:
                right_endpoints.append(right)
            left, right = left+1, right - 1
        elif choice == "left":
            right -= 1
        elif choice == "right":
            left += 1 
        else:
            print("choice:", choice)
            raise AssertionError("invalid choice")
    
    list_indices = left_endpoints + right_endpoints[::-1] 

    print(list_indices)
    print("".join(s[i] for i in list_indices))

if __name__ == '__main__':
    main()
    