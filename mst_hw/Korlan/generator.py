import random

def generator(n: int, p: float) -> list[tuple[int,int,int]]:
    """
    n: number of nodes
    p: probability of inserting an edge
    
    algorithm:
        considers all n*(n-1)/2 and decides for each edge, with probability p
            whether to include it or not
        that means, for every edge:
            - generate a random number $t$ from 0 to 1,
            - if t < p, then include the edge
            - otherwise, exclude it
    """
    assert n >= 1, 'the number of nodes should be at least 1'
    assert 0 < p <= 1, 'the density shoud be in the interval (0, 1]'
    
    if n == 1:
        return []  # No edges for a single node
    
    edges = []
    edge_set = set()  # To avoid duplicate edges
    
    # Create a spanning tree to ensure connectivity
    nodes = list(range(n))
    random.shuffle(nodes)
    
    for i in range(1, n):
        u = random.choice(nodes[:i])
        v = nodes[i]
        weight = random.randint(1, 100)
        if u > v:
            u, v = v, u
        
        edges.append((u, v, weight))
        edge_set.add((u, v))
    
    # Consider all remaining possible edges with probability p
    for i in range(n):
        for j in range(i + 1, n):
            # Skip edges already in spanning tree
            if (i, j) not in edge_set:
                if random.random() < p:
                    weight = random.randint(1, 100)
                    edges.append((i, j, weight))
                    edge_set.add((i, j))
    
    return edges
