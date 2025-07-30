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
        
    algorithm: Kruskal's algorithm
    """
    
    # for this task, you also need to implement the Disjoint Sets data structure
    # it's used in every iteration of Kruskal's algorithm
    pass 
    raise NotImplementedError()

