def validate_mst(n: int, edges_list: list[tuple[int,int,int]], mst_edges_idx: list[int]) -> bool:
    """
    n: number of nodes
    edges_list: list of edges in the graph.
        Each edge is a tuple (a,b,w)
            where a and b are the labels of the vertices
            and w is the weight of that edge
    
    mst_edges_idx: a list of indices of the edges in the mst
    
    return: true if mst_edges_idx is a valid MST, false otherwise    
    """
    
    # step 1. validate that the indices in mst_edges_idx are from 0 to len(edges_list) - 1
    # step 2. validate that mst_edges_idx is a tree (...)
    # step 3. validate that it is a MST (each edge is optimal)
    
    raise NotImplementedError()