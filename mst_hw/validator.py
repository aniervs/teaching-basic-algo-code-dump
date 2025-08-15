def validate_mst(n: int, edges_list: list[tuple[int, int, int]], mst_edges_idx: list[int]) -> bool:
    """
    Validate if the given edge indices form a valid Minimum Spanning Tree.
    
    Args:
        n: number of nodes (0 to n-1)
        edges_list: list of all edges in the graph as (u, v, weight) tuples
        mst_edges_idx: list of indices pointing to edges in edges_list that form the MST
    
    Returns:
        True if mst_edges_idx represents a valid MST, False otherwise
    """
    # Validate indices and extract MST edges
    if not all(0 <= idx < len(edges_list) for idx in mst_edges_idx):
        return False
    
    if len(set(mst_edges_idx)) != len(mst_edges_idx):  # Check for duplicates
        return False
        
    mst_edges = [edges_list[idx] for idx in mst_edges_idx]
    
    # Check if it forms a spanning tree (n-1 edges, connected, acyclic)
    if len(mst_edges) != n - 1:
        return False
    
    # Check connectivity using Union-Find
    if not is_connected(mst_edges, n):
        return False
    
    # Check if it's a minimum spanning tree using cycle property
    # For each edge NOT in MST, adding it should create a cycle where
    # the MST edge in that cycle has weight <= the added edge's weight
    
    mst_edge_set = set(mst_edges)
    
    for edge in edges_list:
        if edge not in mst_edge_set:
            # Add this edge to MST - it creates exactly one cycle
            cycle_edges = find_cycle_edges(mst_edges + [edge], n)
            if not cycle_edges:
                continue  
                
            # Find the heaviest edge in the cycle
            max_weight_in_cycle = max(e[2] for e in cycle_edges)
            
            # If the added edge is lighter than some MST edge in the cycle,
            # then our MST is not minimal
            if edge[2] < max_weight_in_cycle and any(e in mst_edge_set and e[2] > edge[2] for e in cycle_edges):
                return False
    
    return True


def is_connected(edges: list[tuple[int, int, int]], n: int) -> bool:
    """Check if the given edges connect all n vertices."""
    if not edges:
        return n <= 1
        
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False
    
    components = n
    for u, v, _ in edges:
        if union(u, v):
            components -= 1
    
    return components == 1


def find_cycle_edges(edges: list[tuple[int, int, int]], n: int) -> list[tuple[int, int, int]]:
    """
    Find edges that form a cycle when added to a tree.
    Returns the edges forming the unique cycle.
    """
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Find cycle using DFS
    visited = [False] * n
    parent = [-1] * n
    cycle_edges = []
    
    def dfs(node, par):
        visited[node] = True
        for neighbor, weight in adj[node]:
            if neighbor == par:
                continue
            if visited[neighbor]:
                # Found back edge - trace cycle
                curr = node
                while curr != neighbor:
                    for next_node, w in adj[curr]:
                        if next_node == parent[curr]:
                            cycle_edges.append((min(curr, next_node), max(curr, next_node), w))
                            break
                    curr = parent[curr]
                # Add the back edge
                cycle_edges.append((min(node, neighbor), max(node, neighbor), weight))
                return True
            else:
                parent[neighbor] = node
                if dfs(neighbor, node):
                    return True
        return False
    
    # Start DFS from vertex 0
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                break
    
    return cycle_edges