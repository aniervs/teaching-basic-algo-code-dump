from collections import defaultdict

# DFS to find path between nodes
def dfs_find_path(adj: defaultdict, current: int, target: int, visited: set, path: list[int]) -> bool:
    if current == target:
        return True
    visited.add(current)
    for neighbor, e_idx in adj[current]:
        if neighbor not in visited:
            path.append(e_idx)
            if dfs_find_path(neighbor, target, visited, path):
                return True
            path.pop()
    return False

# Function to extract the heaviest edge in path
def find_heaviest_edge(graph: list[tuple[int,int,int]], edges: list[int]) -> tuple[int,int]:
    max_weight = -1
    max_edge_idx = -1
    for e_idx in edges:
        a, b, w = graph[e_idx]
        if w > max_weight:
            max_weight = w
            max_edge_idx = e_idx
    return max_edge_idx, max_weight

def add_edge(n: int, graph: list[tuple[int,int,int]], mst_edges_indices: list[int], new_edge: tuple[int,int,int]) -> list[int]:
    """
    Adds a new edge between existing vertices and updates the MST.
    
    Args:
        n: Number of vertices (0 to n-1)
        graph: Original graph edges (a, b, w)
        mst_edges_indices: Current MST as indices of edges in original graph
        new_edge: New edge to add (a, b, w)
        
    Returns:
        Updated MST edge indices
    """
    # Add new edge to graph and get its index
    new_edge_index = len(graph)
    updated_graph = graph + [new_edge]
    
    # Build adjacency list for current MST
    adj = defaultdict(list)
    for idx in mst_edges_indices:
        a, b, w = graph[idx]
        adj[a].append((b, idx))
        adj[b].append((a, idx))
    
    # Find the path edges
    start, end, _ = new_edge
    path_edges = []
    visited = set()
    dfs_find_path(adj, start, end, visited, path_edges)
    
    max_edge_idx, max_weight = find_heaviest_edge(graph, path_edges)
    
    # Update MST if needed
    if new_edge[2] < max_weight:
        return [idx for idx in mst_edges_indices if idx != max_edge_idx] + [new_edge_index]
    return mst_edges_indices
