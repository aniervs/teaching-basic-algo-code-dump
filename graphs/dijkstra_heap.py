
import heapq

def dijkstra(n: int, source: int, adj_list: list[list[tuple[int,int]]]) -> list[int]:
    """
    n: number of vertices 
    source: source vertex
    adj_list[u] contains a list of tuples (v, w) meaning there is an edge from u to v with weight w
    return: a list prev[] where prev[u] indicates what's the previous vertex on the optimal path from source to u
    
    runs a greedy algorithm that always retrieves the unprocessed vertex with the least d, and relax the edges
    """
    
    distance = [float("inf") for _ in range(n)]
    distance[source] = 0
    processed = [False for _ in range(n)]
    
    priority_queue = [(distance[source], source)]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 0:
        # find the unprocessed vertex with the least distance
        d_u, u = heapq.heappop(priority_queue) # extract u from the priority queue
            
        if d_u > distance[u] or processed[u]:
            continue
                    
        processed[u] = True 
        
        for v, w in adj_list[u]:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w 
                heapq.heappush(priority_queue, (distance[v], v))
        
    print(distance)

def main():
    n, m = map(int, input().split()) # num of vertices and edges respectively
    # assume that the vertices are labeled from 0 to n - 1
    adj_list = [[] for _ in range(n)] # initially, each vertex has 0 neighbors
    
    # read the edges (directed edges)
    for _ in range(m):
        u, v, w = map(int, input().split()) # a directed edge u -> v with weight = w
        adj_list[u].append((v, w)) # v is a neighbor of u and the edge has weight w 
    
    dijkstra(n, 0, adj_list)
    
    
    

if __name__ == '__main__':
    main()


