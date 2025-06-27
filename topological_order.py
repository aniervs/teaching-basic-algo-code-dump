adj_list = []
visited = []
topological_order = []

def dfs(node: int):
    visited[node] = True 
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor)
    topological_order.append(node)

def main():
    global adj_list, visited
    
    n_nodes, n_edges = map(int, input().split())
    adj_list = [[] for _ in range(n_nodes)]
    visited = [False for _ in range(n_nodes)]
    for _ in range(n_edges):
        a, b = map(int, input().split()) # a --> b 
        adj_list[a].append(b) # only this one 'cause the graph is directed
    
    for node in range(n_nodes):
        if not visited[node]:
            dfs(node)
            
    print(topological_order)
    
if __name__ == '__main__':
    main()