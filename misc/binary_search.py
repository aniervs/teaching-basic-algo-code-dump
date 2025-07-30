arr = list(map(int, input().split()))
n = len(arr)
x = int(input())

l, r = 0, n

while r - l > 1:
    m = (l + r) // 2 # m is the middle position
    if arr[m] >= x:
        r = m 
    else:
        l = m 

print(r) # r will consist of the first position with a number >= x