from kruskal import DisjointSets

def kruskal_range_1_to_n(n: int, edges_list: list[tuple[int,int,int]]) -> list[int]:
    """
    Optimized Kruskal's algorithm when edge weights are integers in range [1, n].
    Uses counting sort to achieve O(m + n + m α(n)) = O(m α(n)) time complexity.
    
    Args:
        n: number of nodes (0 to n-1)
        edges_list: list of edges as (u, v, weight) where weight ∈ [1, n]
    
    Returns:
        List of edge indices forming the MST
    """
    if n <= 1:
        return []
    
    # Step 1: Counting sort by weight - O(m + n)
    # Create buckets for each possible weight [1, n]
    buckets = [[] for _ in range(n + 1)]  # buckets[0] unused
    
    for idx, (u, v, weight) in enumerate(edges_list):
        buckets[weight].append((u, v, idx))
    
    # Step 2: Extract edges in sorted order - O(m)
    sorted_edges = []
    for weight in range(1, n + 1):
        for u, v, original_idx in buckets[weight]:
            sorted_edges.append((u, v, weight, original_idx))
    
    # Step 3: Standard Kruskal's with sorted edges - O(m α(n))
    ds = DisjointSets(n)
    mst_edges = []
    
    for u, v, weight, original_idx in sorted_edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append(original_idx)
            
            # Early termination: MST has exactly n-1 edges
            if len(mst_edges) == n - 1:
                break
    
    return mst_edges


def kruskal_range_1_to_W(n: int, edges_list: list[tuple[int,int,int]], W: int) -> list[int]:
    """
    Optimized Kruskal's algorithm when edge weights are integers in range [1, W] 
    for constant W. Uses counting sort to achieve O(m + W + m α(n)) = O(m α(n)) time.
    
    Args:
        n: number of nodes (0 to n-1)
        edges_list: list of edges as (u, v, weight) where weight ∈ [1, W]
        W: maximum weight value (constant)
    
    Returns:
        List of edge indices forming the MST
    """
    if n <= 1:
        return []
    
    # Step 1: Counting sort by weight - O(m + W)
    # Since W is constant, this is O(m)
    buckets = [[] for _ in range(W + 1)]  # buckets[0] unused
    
    for idx, (u, v, weight) in enumerate(edges_list):
        buckets[weight].append((u, v, idx))
    
    # Step 2: Extract edges in sorted order - O(m)
    sorted_edges = []
    for weight in range(1, W + 1):
        for u, v, original_idx in buckets[weight]:
            sorted_edges.append((u, v, weight, original_idx))
    
    # Step 3: Standard Kruskal's with sorted edges - O(m α(n))
    ds = DisjointSets(n)
    mst_edges = []
    
    for u, v, weight, original_idx in sorted_edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append(original_idx)
            
            # Early termination: MST has exactly n-1 edges
            if len(mst_edges) == n - 1:
                break
    
    return mst_edges


def benchmark_optimized_kruskal():
    """
    Benchmark to demonstrate the improvement of optimized Kruskal's algorithms.
    """
    import time
    from generator import generator
    from kruskal import kruskal
    
    print("=== Optimized Kruskal's Algorithm Benchmark ===\n")
    
    # Test with different graph sizes
    for n in [50, 100, 200]:
        print(f"Testing with n = {n} nodes:")
        
        # Generate graph with weights in [1, n]
        edges = []
        for _ in range(3):  # Average over multiple trials
            test_edges = generator(n, p=0.3, weight_range=(1, n))
            if len(test_edges) >= n - 1:
                edges = test_edges
                break
        
        if not edges:
            print(f"  Skipping n={n} - no connected graph generated")
            continue
            
        print(f"  Graph has {len(edges)} edges")
        
        # Standard Kruskal's
        start = time.perf_counter()
        mst_standard = kruskal(n, edges)
        time_standard = (time.perf_counter() - start) * 1000
        
        # Optimized Kruskal's (weights in [1, n])
        start = time.perf_counter()
        mst_optimized_n = kruskal_range_1_to_n(n, edges)
        time_optimized_n = (time.perf_counter() - start) * 1000
        
        # Optimized Kruskal's (weights in [1, W] with W=10)
        # First modify weights to be in [1, 10]
        edges_W = [(u, v, (w % 10) + 1) for u, v, w in edges]
        start = time.perf_counter()
        mst_optimized_W = kruskal_range_1_to_W(n, edges_W, W=10)
        time_optimized_W = (time.perf_counter() - start) * 1000
        
        # Verify correctness
        from validator import validate_mst
        assert validate_mst(n, edges, mst_standard)
        assert validate_mst(n, edges, mst_optimized_n)
        assert validate_mst(n, edges_W, mst_optimized_W)
        
        print(f"  Standard Kruskal's:      {time_standard:.3f} ms")
        print(f"  Optimized [1,n]:         {time_optimized_n:.3f} ms ({time_standard/time_optimized_n:.1f}x speedup)")
        print(f"  Optimized [1,W] (W=10):  {time_optimized_W:.3f} ms ({time_standard/time_optimized_W:.1f}x speedup)")
        print()


if __name__ == "__main__":
    benchmark_optimized_kruskal()