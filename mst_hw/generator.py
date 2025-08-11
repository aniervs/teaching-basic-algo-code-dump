import random

def generator(n: int, p: float) -> list[tuple[int, int, int]]:
    """
    n: number of nodes
    p: probability of inserting an edge
    
    Generates a connected graph with n nodes and edge density controlled by p.
    """
    assert n >= 1, 'the number of nodes should be at least 1'
    assert 0 < p <= 1, 'the density should be in the interval (0, 1]'
    
    edges = []
    
    # Step 1: Create a spanning tree to ensure the graph is connected
    nodes = list(range(n))
    random.shuffle(nodes)
    for i in range(1, n):
        u = nodes[i - 1]
        v = nodes[i]
        w = random.randint(1, 10)  # Random weight between 1 and 10
        edges.append((u, v, w))
    
    # Step 2: Add additional edges with probability p
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:
                w = random.randint(1, 10)  # Random weight between 1 and 10
                edges.append((u, v, w))
    
    return edges
