adj_list = []
visited = []

current_connected_component = []

# depth-first search
def dfs(node: int):
    current_connected_component.append(node)
    visited[node] = True 
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor)

def main():
    global adj_list, visited
    n_nodes, n_edges = map(int, input().split())
    # assume the nodes are indexed from 0 to n_nodes - 1
    
    adj_list = [[] for _ in range(n_nodes)] # initially, every node has an empty list of neighbors
    visited = [False for _ in range(n_nodes)] # initially, every node isn't visited
    
    
    # reading all the edges
    for _ in range(n_edges):
        a, b = map(int, input().split()) # a and b are a pair of vertices that are adjacent
        adj_list[a].append(b)
        adj_list[b].append(a) # this is only if the graph is undirected (bidirectional)
    
    for node in range(n_nodes):
        if not visited[node]:
            current_connected_component.clear() # I'm resetting to empty the list of nodes in the current node 
            dfs(node) # this will expand thruogh the connected component of that node
            print("connected component:", current_connected_component)
        
            
if __name__ == '__main__':
    main()
