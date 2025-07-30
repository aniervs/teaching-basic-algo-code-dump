

def bellman_ford(n: int, source: int, adj_list: list[list[tuple[int,int]]]) -> list[int]:
    """
    n: number of vertices 
    source: source vertex
    adj_list[u] contains a list of tuples (v, w) meaning there is an edge from u to v with weight w
    return: a list prev[] where prev[u] indicates what's the previous vertex on the optimal path from source to u
    
    runs dynamic programming to find the shortest path from the source (s) to all other vertices
    """
    
    distance = [float("inf") for _ in range(n)]
    distance[source] = 0
    
    prev = [None for _ in range(n)]
    
    for k in range(n - 1):
        for v in range(n):
            for u, w in adj_list[v]:
                # there is an edge from v to u with weight w 
                if distance[u] > distance[v] + w:
                    distance[u] = distance[v] + w 
                    prev[u] = v 
    
    print(distance)
    return prev

def main():
    n, m = map(int, input().split()) # num of vertices and edges respectively
    # assume that the vertices are labeled from 0 to n - 1
    adj_list = [[] for _ in range(n)] # initially, each vertex has 0 neighbors
    
    # read the edges (directed edges)
    for _ in range(m):
        u, v, w = map(int, input().split()) # a directed edge u -> v with weight = w
        adj_list[u].append((v, w)) # v is a neighbor of u and the edge has weight w 
    
    prev = bellman_ford(n, 0, adj_list)
    print(prev)
    
    
    

if __name__ == '__main__':
    main()


