

def floyd_warshall(n: int, adj_list: list[list[tuple[int,int]]]) -> list[int]:
    """
    n: number of vertices 
    adj_list[u] contains a list of tuples (v, w) meaning there is an edge from u to v with weight w
    return: a 2D array parent[u,v] : an intermediate vertex in the optimal path from u to v 
    """
    
    distance = [
            [float("inf") for _ in range(n)]
        for _ in range(n)
    ] # initially, d[u,v] = inf for every pair u,v
    
    parent = [
            [None for _ in range(n)]
        for _ in range(n)
    ] # which intermediate vertex i to take so that we go u->...->i->...->v
    
    # for the edges u->v with weight w, set the distance to be w 
    for u in range(n):
        for v, w in adj_list[u]:
            distance[u][v] = w 
            parent[u][v] = u 
            
    # distance[u][u] = 0
    for u in range(n):
        distance[u][u] = 0
        parent[u][u] = u
        
    for i in range(n):
        for u in range(n):
            for v in range(n):
                if distance[u][v] > distance[u][i] + distance[i][v]:
                    distance[u][v] = distance[u][i] + distance[i][v]
                    # parent[u][v] = something.... #TODO
                    
    return parent 
    

def main():
    n, m = map(int, input().split()) # num of vertices and edges respectively
    # assume that the vertices are labeled from 0 to n - 1
    adj_list = [[] for _ in range(n)] # initially, each vertex has 0 neighbors
    
    # read the edges (directed edges)
    for _ in range(m):
        u, v, w = map(int, input().split()) # a directed edge u -> v with weight = w
        adj_list[u].append((v, w)) # v is a neighbor of u and the edge has weight w 
    
    parent = floyd_warshall(n, adj_list)
    
    # given u and v, reconstruct the optimal path from u to v...
    # TODO
    
    # print(parent)
    
    
    
    

if __name__ == '__main__':
    main()


