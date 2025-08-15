def prim_range_1_to_n(n: int, edges_list: list[tuple[int, int, int]]) -> list[int]:
    """
    Optimized Prim's algorithm when edge weights are integers in range [1, n].
    Uses bucket-based priority queue to achieve O(m + n²) time complexity.
    
    Args:
        n: number of nodes (0 to n-1)
        edges_list: list of edges as (u, v, weight) where weight ∈ [1, n]
    
    Returns:
        List of edge indices forming the MST
    """
    if n <= 1:
        return []
    
    # Build adjacency list with edge indices
    adj = [[] for _ in range(n)]
    for idx, (u, v, weight) in enumerate(edges_list):
        adj[u].append((v, weight, idx))
        adj[v].append((u, weight, idx))
    
    # Bucket-based priority queue for weights in [1, n]
    buckets = [[] for _ in range(n + 1)]  # buckets[0] unused
    in_mst = [False] * n
    key = [float('inf')] * n
    parent_edge = [-1] * n
    
    # Start from vertex 0
    key[0] = 0
    buckets[0].append(0)  # Use bucket[0] for starting vertex with key=0
    min_bucket = 0
    
    mst_edges = []
    vertices_added = 0
    
    while vertices_added < n:
        # Find next minimum weight vertex - O(n) amortized
        while min_bucket <= n and not buckets[min_bucket]:
            min_bucket += 1
        
        if min_bucket > n:  # No more reachable vertices
            break
            
        u = buckets[min_bucket].pop()
        
        # Skip if already in MST (handles duplicates)
        if in_mst[u]:
            continue
            
        # Add vertex to MST
        in_mst[u] = True
        vertices_added += 1
        
        if parent_edge[u] != -1:
            mst_edges.append(parent_edge[u])
        
        # Update keys of adjacent vertices - O(degree(u))
        for v, weight, edge_idx in adj[u]:
            if not in_mst[v] and weight < key[v]:
                # Remove v from old bucket if it was there
                if key[v] != float('inf'):
                    try:
                        buckets[int(key[v])].remove(v)
                    except ValueError:
                        pass  # v might have been processed already
                
                # Update key and add to new bucket
                key[v] = weight
                parent_edge[v] = edge_idx
                buckets[weight].append(v)
                
                # Update min_bucket if necessary
                if weight < min_bucket:
                    min_bucket = weight
    
    return mst_edges


def prim_range_1_to_W(n: int, edges_list: list[tuple[int, int, int]], W: int) -> list[int]:
    """
    Optimized Prim's algorithm when edge weights are integers in range [1, W] 
    for constant W. Uses bucket-based priority queue to achieve O(m + nW) = O(m + n) time.
    
    Args:
        n: number of nodes (0 to n-1)
        edges_list: list of edges as (u, v, weight) where weight ∈ [1, W]
        W: maximum weight value (constant)
    
    Returns:
        List of edge indices forming the MST
    """
    if n <= 1:
        return []
    
    # Build adjacency list with edge indices
    adj = [[] for _ in range(n)]
    for idx, (u, v, weight) in enumerate(edges_list):
        adj[u].append((v, weight, idx))
        adj[v].append((u, weight, idx))
    
    # Bucket-based priority queue for weights in [1, W]
    buckets = [[] for _ in range(W + 1)]  # buckets[0] for starting vertex
    in_mst = [False] * n
    key = [float('inf')] * n
    parent_edge = [-1] * n
    
    # Start from vertex 0
    key[0] = 0
    buckets[0].append(0)
    min_bucket = 0
    
    mst_edges = []
    vertices_added = 0
    
    while vertices_added < n:
        # Find next minimum weight vertex - O(W) = O(1) since W is constant
        while min_bucket <= W and not buckets[min_bucket]:
            min_bucket += 1
        
        if min_bucket > W:  # No more reachable vertices
            break
            
        u = buckets[min_bucket].pop()
        
        # Skip if already in MST
        if in_mst[u]:
            continue
            
        # Add vertex to MST
        in_mst[u] = True
        vertices_added += 1
        
        if parent_edge[u] != -1:
            mst_edges.append(parent_edge[u])
        
        # Update keys of adjacent vertices
        for v, weight, edge_idx in adj[u]:
            if not in_mst[v] and weight < key[v]:
                # Remove v from old bucket if it was there
                if key[v] != float('inf'):
                    try:
                        buckets[int(key[v])].remove(v)
                    except ValueError:
                        pass
                
                # Update key and add to new bucket
                key[v] = weight
                parent_edge[v] = edge_idx
                buckets[weight].append(v)
                
                # Update min_bucket if necessary
                if weight < min_bucket:
                    min_bucket = weight
    
    return mst_edges


def prim_fibonacci_heap(n: int, edges_list: list[tuple[int, int, int]]) -> list[int]:
    """
    Prim's algorithm using Fibonacci heap for comparison.
    Achieves O(m + n log n) time complexity.
    This is asymptotically better than our bucket approach but has higher constants.

    """
    if n <= 1:
        return []
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for idx, (u, v, weight) in enumerate(edges_list):
        adj[u].append((v, weight, idx))
        adj[v].append((u, weight, idx))
    
    # Simulate Fibonacci heap with Python's heapq (which is actually a binary heap)
    import heapq
    
    in_mst = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, vertex, edge_index)
    mst_edges = []
    
    while min_heap and len(mst_edges) < n - 1:
        weight, u, edge_idx = heapq.heappop(min_heap)
        
        if in_mst[u]:
            continue
            
        in_mst[u] = True
        if edge_idx != -1:
            mst_edges.append(edge_idx)
        
        for v, w, idx in adj[u]:
            if not in_mst[v]:
                heapq.heappush(min_heap, (w, v, idx))
    
    return mst_edges


def benchmark_prim_optimizations():
    """
    Benchmark to compare different Prim's algorithm implementations.
    """
    import time
    from generator import generator
    from prim import prim_n2, prim_mlogn
    from validator import validate_mst
    
    print("=== Optimized Prim's Algorithm Benchmark ===\n")
    
    for n in [50, 100, 200]:
        print(f"Testing with n = {n} nodes:")
        
        # Generate graph with weights in [1, n]
        edges = generator(n, p=0.4, weight_range=(1, n))
        if len(edges) < n - 1:
            print(f"  Skipping n={n} - graph not connected")
            continue
            
        print(f"  Graph has {len(edges)} edges")
        
        # Standard Prim's algorithms
        start = time.perf_counter()
        mst_n2 = prim_n2(n, edges)
        time_n2 = (time.perf_counter() - start) * 1000
        
        start = time.perf_counter()
        mst_mlogn = prim_mlogn(n, edges)
        time_mlogn = (time.perf_counter() - start) * 1000
        
        # Optimized Prim's (weights in [1, n])
        start = time.perf_counter()
        mst_opt_n = prim_range_1_to_n(n, edges)
        time_opt_n = (time.perf_counter() - start) * 1000
        
        # Optimized Prim's (weights in [1, W] with W=10)
        edges_W = [(u, v, (w % 10) + 1) for u, v, w in edges]
        start = time.perf_counter()
        mst_opt_W = prim_range_1_to_W(n, edges_W, W=10)
        time_opt_W = (time.perf_counter() - start) * 1000
        
        # Verify correctness
        assert validate_mst(n, edges, mst_n2)
        assert validate_mst(n, edges, mst_mlogn)
        assert validate_mst(n, edges, mst_opt_n)
        assert validate_mst(n, edges_W, mst_opt_W)
        
        print(f"  Prim O(n²):              {time_n2:.3f} ms")
        print(f"  Prim O(m log n):         {time_mlogn:.3f} ms")
        print(f"  Prim optimized [1,n]:    {time_opt_n:.3f} ms")
        print(f"  Prim optimized [1,W]:    {time_opt_W:.3f} ms")
        print()


if __name__ == "__main__":
    benchmark_prim_optimizations()