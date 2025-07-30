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
    
    raise NotImplementedError()
