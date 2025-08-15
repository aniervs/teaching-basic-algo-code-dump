def kruskal(n: int, edges_list: list[tuple[int,int,int]]) -> list[int]:
    """
    n: number of nodes (the nodes are labeled from 0 to n - 1)
    edges_list: list of edges in the graph.
        Each edge is a tuple (a,b,w)
            where a and b are the labels of the vertices
            and w is the weight of that edge
    
    return: a list of indices
        each index corresponds to the index of an edge in the original list
        be sure to use the original indices and not the ones of the sorted list
        
    algorithm: Kruskal's algorithm with Disjoint Sets in O(m * log n) time
    """
    if n <= 1:
        return []
    
    # Create indexed edges list to preserve original indices after sorting
    indexed_edges = [(w, a, b, idx) for idx, (a, b, w) in enumerate(edges_list)]
    
    # Sort edges by weight - O(m log m) = O(m log n) since m <= n^2
    indexed_edges.sort()
    
    # Initialize Disjoint Sets
    ds = DisjointSets(n)
    
    mst_edges = []
    edges_added = 0
    
    # Process edges in order of increasing weight
    for weight, u, v, original_idx in indexed_edges:
        # If u and v are in different components, add this edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append(original_idx)
            edges_added += 1
            
            # MST has exactly n-1 edges
            if edges_added == n - 1:
                break
    
    return mst_edges


class DisjointSets:
    """
    Disjoint Sets (Union-Find) data structure with path compression and union by rank.
    Supports near O(1) amortized time for union and find operations.
    """
    
    def __init__(self, n: int):
        """
        Initialize n disjoint sets, each containing one element {0}, {1}, ..., {n-1}
        
        Args:
            n: number of elements (labeled 0 to n-1)
        """
        self.parent = list(range(n))  # Initially, each element is its own parent
        self.rank = [0] * n           # Initially, all trees have rank 0
    
    def find(self, x: int) -> int:
        """
        Find the representative (root) of the set containing x.
        Uses path compression for optimization.
        
        Args:
            x: element to find
            
        Returns:
            representative of the set containing x
        """
        if self.parent[x] != x:
            # Path compression: make x point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        """
        Union the sets containing x and y.
        Uses union by rank for optimization.
        
        Args:
            x, y: elements whose sets should be merged
            
        Returns:
            True if sets were different (union performed), False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        # Already in the same set
        if root_x == root_y:
            return False
        
        # Union by rank: attach smaller tree under root of larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Same rank: make y child of x and increase x's rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
    def connected(self, x: int, y: int) -> bool:
        """
        Check if x and y are in the same set.
        
        Args:
            x, y: elements to check
            
        Returns:
            True if x and y are in the same connected component
        """
        return self.find(x) == self.find(y)

