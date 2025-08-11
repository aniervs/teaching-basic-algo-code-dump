
def add_vertex(n: int, graph: list[tuple[int,int,int]], mst: list[int], new_incident_edges: list[tuple[int,int]]):
    """
    Adds a new vertex `n` and its incident edges to the graph, then updates the MST.
    
    Args:
        n: The new vertex label.
        graph: The original graph as a list of edges (u, v, w).
        mst: Current MST as indices of edges in original graph.
        new_incident_edges: Edges connecting `n` to existing vertices (u, n, w).
    
    Returns:
        The updated MST including the new vertex.
        
    The idea:
        The new MST must include exactly one edge from v to the existing tree (to maintain a tree structure).
        The minimum-weight such edge guarantees the MST property.
        Time complexity: O(len(new_incident_edges)).
    """
    
    # Find minimum weight edge connecting new vertex to existing MST
    min_edge_index = None
    min_weight = float('inf')
    
    # Get all nodes in current MST
    mst_nodes = set()
    for edge_idx in mst:
        a, b, w = graph[edge_idx]
        mst_nodes.add(a)
        mst_nodes.add(b)
    
    # Check which new edges connect to MST nodes
    for idx, (a, b, w) in enumerate(new_incident_edges, start=len(graph)):
        other = a if b == n else b
        if other in mst_nodes and w < min_weight:
            min_weight = w
            min_edge_index = idx
    
    if min_edge_index is not None:
        return mst + [min_edge_index]
    else:
        # No valid connection found (shouldn't happen if graph is connected)
        return mst
