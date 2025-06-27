adj_list = []
color = []
is_bipartite = True

def dfs(node: int):
    global is_bipartite
    for neighbor in adj_list[node]:
        if color[neighbor] is None:
            color[neighbor] = not color[node]
            dfs(neighbor)
        elif color[neighbor] == color[node]:
            is_bipartite = False 
            return 

def main():
    n_nodes, n_edges = map(int, input().split())
    adj_list = [[] for _ in range(n_nodes)]
    color = [None for _ in range(n_nodes)]
    
    for _ in range(n_edges):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    for node in range(n_nodes):
        if color[node] is None: # i.e: it hasn't been colored/visited yet
            color[node] = 0
            dfs(node)
        
    if is_bipartite:
        print("it is bipartite")
    else:
        print("it is not bipartite")
    
    

if __name__ == '__main__':
    main()