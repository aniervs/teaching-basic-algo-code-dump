def add_vertex(n: int, graph: list[tuple[int,int,int]], mst: list[int], 
               new_incident_edges: list[tuple[int,int]]) -> tuple[list[tuple[int,int,int]], list[int]]:
    """
    Add a new vertex (labeled n) with incident edges to an existing graph and update the MST.
    
    Args:
        n: number of vertices in current graph (0 to n-1). New vertex will be labeled n.
        graph: current list of edges as (u, v, weight)
        mst: current list of edge indices that form the MST
        new_incident_edges: list of (neighbor_vertex, weight) for edges from new vertex n
    
    Returns:
        tuple (updated_graph, updated_mst_indices)
        - updated_graph: new graph with added vertex and edges
        - updated_mst_indices: indices of edges forming the new MST
    """
    if not new_incident_edges:
        # No edges to add - just return original graph and MST
        return graph.copy(), mst.copy()
    
    # Step 1: Create the updated graph
    updated_graph = graph.copy()
    
    # Add new edges to the graph
    new_edge_start_idx = len(graph)
    for neighbor, weight in new_incident_edges:
        updated_graph.append((n, neighbor, weight))
    
    # Step 2: Find the minimum weight edge connecting new vertex to existing MST
    # Since the existing vertices form a connected MST, any edge from the new vertex
    # to any existing vertex will connect the new vertex to the MST
    min_weight = float('inf')
    min_edge_idx = -1
    
    for i, (neighbor, weight) in enumerate(new_incident_edges):
        if weight < min_weight:
            min_weight = weight
            min_edge_idx = new_edge_start_idx + i
    
    # Step 3: Update MST by adding the minimum weight edge
    updated_mst = mst.copy()
    if min_edge_idx != -1:
        updated_mst.append(min_edge_idx)
    
    return updated_graph, updated_mst

def add_edge(n: int, graph: list[tuple[int,int,int]], mst: list[int], 
             new_edge: tuple[int,int,int]) -> tuple[list[tuple[int,int,int]], list[int]]:
    """
    Add a new edge between existing vertices and update the MST.
    
    Algorithm:
    1. Add the new edge to the graph
    2. Adding this edge creates exactly one cycle in the MST
    3. Find the heaviest edge in this cycle
    4. If new edge is lighter than heaviest edge in cycle, replace it
    
    Args:
        n: number of vertices (0 to n-1)
        graph: current list of edges as (u, v, weight)
        mst: current list of edge indices that form the MST
        new_edge: new edge to add as (u, v, weight)
    
    Returns:
        tuple (updated_graph, updated_mst_indices)
    
    Time Complexity: O(n) - finding the cycle path between two vertices in a tree
    """
    u, v, weight = new_edge
    
    # Step 1: Add new edge to graph
    updated_graph = graph + [new_edge]
    new_edge_idx = len(graph)
    
    # Step 2: Build MST adjacency list for cycle detection
    mst_adj = [[] for _ in range(n)]
    mst_edges = [graph[i] for i in mst]
    
    for i, edge_idx in enumerate(mst):
        a, b, w = graph[edge_idx]
        mst_adj[a].append((b, w, edge_idx))
        mst_adj[b].append((a, w, edge_idx))
    
    # Step 3: Find path between u and v in current MST (this is the cycle when new edge is added)
    path_edges = find_path_in_tree(mst_adj, u, v, n)
    
    if not path_edges:
        # u and v are not connected in current MST (shouldn't happen if MST is valid)
        # Just add the new edge
        return updated_graph, mst + [new_edge_idx]
    
    # Step 4: Find heaviest edge in the cycle (path + new edge)
    max_weight = -1
    max_weight_idx = -1
    max_weight_mst_pos = -1
    
    for edge_idx in path_edges:
        edge_weight = graph[edge_idx][2]
        if edge_weight > max_weight:
            max_weight = edge_weight
            max_weight_idx = edge_idx
    
    # Step 5: Decide whether to replace heaviest edge with new edge
    if weight < max_weight:
        # New edge is better - replace heaviest edge in cycle
        updated_mst = [idx if idx != max_weight_idx else new_edge_idx for idx in mst]
    else:
        # Keep current MST - new edge doesn't improve it
        updated_mst = mst.copy()
    
    return updated_graph, updated_mst