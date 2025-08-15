import random
from typing import List, Tuple

def generator(n: int, p: float, weight_range: Tuple[int, int] = (1, 10000), seed: int = None) -> List[Tuple[int, int, int]]:
    """
    Generate a connected undirected weighted graph with n vertices.
    
    Args:
        n: Number of vertices (labeled 0 to n-1)
        p: Probability of including each edge (0 <= p <= 1)
        weight_range: Range for random edge weights (min, max)
        seed: Random seed for reproducibility
        
    Returns:
        List of edges as tuples (u, v, weight) where u < v
    """
    if seed is not None:
        random.seed(seed)
        
    if n <= 0:
        return []
    if n == 1:
        return []
        
    # Validate inputs
    if not 0 <= p <= 1:
        raise ValueError("p must be between 0 and 1")
        
    min_weight, max_weight = weight_range
    edges = []
    
    # Create a spanning tree to ensure connectivity
    # Use a random permutation to create a random spanning tree
    vertices = list(range(n))
    random.shuffle(vertices)
    
    # Connect consecutive vertices in the shuffled order
    tree_edges = set()
    for i in range(n - 1):
        u, v = vertices[i], vertices[i + 1]
        if u > v:
            u, v = v, u  # Ensure u < v
        weight = random.randint(min_weight, max_weight)
        edges.append((u, v, weight))
        tree_edges.add((u, v))
    
    # Add remaining edges with adjusted probability
    
    total_possible = n * (n - 1) // 2
    remaining_possible = total_possible - (n - 1)
    
    if remaining_possible > 0:
        # Calculate adjusted probability for remaining edges
        expected_total = p * total_possible
        expected_remaining = expected_total - (n - 1)
        
        if expected_remaining > 0:
            q = min(1.0, expected_remaining / remaining_possible)
        else:
            q = 0.0
            
        # Add remaining edges with probability q
        for u in range(n):
            for v in range(u + 1, n):
                if (u, v) not in tree_edges:
                    if random.random() < q:
                        weight = random.randint(min_weight, max_weight)
                        edges.append((u, v, weight))
    
    return edges
