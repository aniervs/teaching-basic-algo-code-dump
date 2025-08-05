import heapq
from .generator import generator, random
from .validator import validate_mst

def prim_n2(n: int, edges_list: list[tuple[int,int,int]]) -> list[int]:
    """
    n: number of nodes (the nodes are labeled from 0 to n - 1)
    edges_list: list of edges in the graph.
        Each edge is a tuple (a,b,w)
            where a and b are the labels of the vertices
            and w is the weight of that edge
    
    return: a list of indices
        each index corresponds to the index of an edge in the original list
        be sure to use the original indices and not the ones of the sorted list
        
    algorithm: Prim's algorithm without priority queue, in O(n^2) time
    """
    
    in_mst = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n
    edge_indices = [-1] * n
    
    # Start with node 0
    min_edge[0] = 0
    
    mst_edges = []
    
    for _ in range(n):
        u = -1
        for v in range(n):
            if not in_mst[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v
        
        if u == -1:
            break
        
        in_mst[u] = True
        
        # Add the edge to the MST if it's not the starting node
        if parent[u] != -1:
            mst_edges.append(edge_indices[u])
        
        # Update the minimum edge weights for the adjacent nodes
        for idx, (a, b, w) in enumerate(edges_list):
            if a == u or b == u:
                v = b if a == u else a
                if not in_mst[v] and w < min_edge[v]:
                    min_edge[v] = w
                    parent[v] = u
                    edge_indices[v] = idx
    
    return mst_edges


def prim_mlogn(n: int, edges_list: list[tuple[int,int,int]]) -> list[int]:
    """
    n: number of nodes (the nodes are labeled from 0 to n - 1)
    edges_list: list of edges in the graph.
        Each edge is a tuple (a,b,w)
            where a and b are the labels of the vertices
            and w is the weight of that edge
    
    return: a list of indices
        each index corresponds to the index of an edge in the original list
        be sure to use the original indices and not the ones of the sorted list
        
    algorithm: Prim's algorithm with priority queue, in O(m \log n) time
    """
    
    # Build adjacency list (for convenience)
    adj = [[] for _ in range(n)]
    for idx, (a, b, w) in enumerate(edges_list):
        adj[a].append((b, w, idx))
        adj[b].append((a, w, idx))
    
    in_mst = [False] * n
    mst_edges = []
    heap = []
    
    # Start with node 0
    in_mst[0] = True
    for (v, w, idx) in adj[0]:
        heapq.heappush(heap, (w, v, idx))
    
    while heap and len(mst_edges) < n - 1:
        w, u, idx = heapq.heappop(heap)
        if not in_mst[u]:
            in_mst[u] = True
            mst_edges.append(idx)
            for (v, w_new, idx_new) in adj[u]:
                if not in_mst[v]:
                    heapq.heappush(heap, (w_new, v, idx_new))
    
    return mst_edges

def stress_test():
    random.seed(42)
    test_cases = 10
    for _ in range(test_cases):
        n = random.randint(1, 20)
        p = random.uniform(0.3, 0.8)
        edges = generator(n, p)
        # mst_indices = prim_n2(n, edges)
        mst_indices = prim_mlogn(n, edges)
        is_valid = validate_mst(n, edges, mst_indices)
        print(f"Test case with n={n}, p={p:.2f}: {'Valid' if is_valid else 'Invalid'} MST")
        if not is_valid:
            print("Invalid MST found!")
            break
     
     
if __name__ == "__main__":   
    stress_test()