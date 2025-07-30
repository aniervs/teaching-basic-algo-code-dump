adj_list = []
visited = []
pred = []

furthest1 = None 
dist_furthest1 = -1

def dfs1(node: int, distance = 0):
    global dist_furthest1, furthest1
    if dist_furthest1 < distance:
        dist_furthest1 = distance 
        furthest1 = node 
        
    visited[node] = True 
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs1(neighbor, distance + 1)

real_furthest = None 
dist_real_furthest = -1
def dfs2(node: int, distance = 0):
    global real_furthest, dist_real_furthest
    if dist_real_furthest < distance:
        dist_real_furthest = distance 
        real_furthest = node 
    
    visited[node] = True 
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            pred[neighbor] = node 
            dfs2(neighbor, distance + 1)

def main():
    global adj_list, visited, pred
    # read a tree, thus the number of edges == n_nodes - 1
    n_nodes = int(input()) 
    adj_list = [[] for _ in range(n_nodes)]
    visited = [False for _ in range(n_nodes)]
    pred = [None for _ in range(n_nodes)]
    
    for _ in range(n_nodes - 1):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    dfs1(0)
    visited = [False for _ in range(n_nodes)]
    dfs2(furthest1)
    
    print("length of the diameter:", dist_real_furthest)
    diameter = []
    
    node = real_furthest
    while node != furthest1:
        diameter.append(node)
        node = pred[node]
    diameter.append(furthest1)
    
    print("actual diameter:", diameter)
    
if __name__ == '__main__':
    main()