import heapq

def prim_n2(n: int, edges_list: list[tuple[int, int, int]]) -> list[int]:
    """
    n: number of nodes (the nodes are labeled from 0 to n - 1)
    edges_list: list of edges in the graph.
        Each edge is a tuple (a, b, w)
            where a and b are the labels of the vertices
            and w is the weight of that edge
    
    return: a list of indices
        each index corresponds to the index of an edge in the original list
        be sure to use the original indices and not the ones of the sorted list
        
    algorithm: Prim's algorithm without priority queue, in O(n^2) time
    """
    if n <= 1:
        return []
    
    #Initialize keys, parents, and visited set
    key = [float('inf')] * n  
    parent = [-1] * n         
    in_mst = [False] * n      
    # Start from the first node
    key[0] = 0

    # Iterate to find the MST
    for _ in range(n):
        # Find the node with the smallest key value that is not in the MST
        u = -1
        min_key = float('inf')
        for i in range(n):
            if not in_mst[i] and key[i] < min_key:
                min_key = key[i]
                u = i

        # If no node is reachable, the graph is disconnected
        if u == -1 or min_key == float('inf'):
            break

        in_mst[u] = True

        for idx, (a, b, w) in enumerate(edges_list):
            if a == u or b == u:  # Check if the edge is connected to u
                v = b if a == u else a
                if not in_mst[v] and w < key[v]:
                    key[v] = w
                    parent[v] = idx

    # Collect the indices of the edges in the MST
    mst_edges_idx = []
    for i in range(1, n):
        if parent[i] != -1:
            mst_edges_idx.append(parent[i])

    return mst_edges_idx

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
        
    algorithm: Prim's algorithm with priority queue, in O(m * log n) time
    """
    if n <= 1:
        return []
    
    # Build adjacency list with edge indices
    adj = [[] for _ in range(n)]
    for idx, (a, b, w) in enumerate(edges_list):
        adj[a].append((b, w, idx))
        adj[b].append((a, w, idx))
    
    # Initialize data structures
    in_mst = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, vertex, edge_index)
    mst_edges = []
    
    # Main algorithm loop
    while min_heap and len(mst_edges) < n - 1:
        weight, u, edge_idx = heapq.heappop(min_heap)
        
        # Skip if vertex already in MST (handles duplicate entries)
        if in_mst[u]:
            continue
            
        # Add vertex to MST
        in_mst[u] = True
        if edge_idx != -1:  # Skip the starting vertex (has no incoming edge)
            mst_edges.append(edge_idx)
        
        # Add all edges from u to vertices not yet in MST
        for v, w, idx in adj[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (w, v, idx))
    
    return mst_edges

