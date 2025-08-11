def validate_mst(n: int, edges_list: list[tuple[int, int, int]], mst_edges_idx: list[int]) -> bool:
    """
    n: number of nodes
    edges_list: list of edges in the graph.
        Each edge is a tuple (a, b, w)
            where a and b are the labels of the vertices
            and w is the weight of that edge
    
    mst_edges_idx: a list of indices of the edges in the mst
    
    return: true if mst_edges_idx is a valid MST, false otherwise    
    """
    # Step 1: Validate that the indices in mst_edges_idx are valid
    if not all(0 <= idx < len(edges_list) for idx in mst_edges_idx):
        return False

    # Extract the edges in the MST
    mst_edges = [edges_list[idx] for idx in mst_edges_idx]

    # Step 2: Validate that mst_edges_idx forms a tree
    if len(mst_edges) != n - 1:
        return False

    # Check if the graph is connected using Union-Find
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for u, v, _ in mst_edges:
        union(u, v)

    # Check if all nodes are connected
    root_set = {find(i) for i in range(n)}
    if len(root_set) != 1:
        return False

    # Step 3: Validate that it is a Minimum Spanning Tree
    # Sort edges by weight
    sorted_edges = sorted(edges_list, key=lambda x: x[2])

    # Check if replacing any edge in the MST with a lighter edge violates the MST property
    mst_weight = sum(w for _, _, w in mst_edges)
    for u, v, w in mst_edges:
        # Remove the edge and check if a lighter edge can replace it
        for edge in sorted_edges:
            if edge not in mst_edges and edge[2] < w:
                # Check if replacing this edge still forms a spanning tree
                temp_edges = [e for e in mst_edges if e != (u, v, w)] + [edge]
                if is_spanning_tree(temp_edges, n):
                    return False

    return True


def is_spanning_tree(edges: list[tuple[int, int, int]], n: int) -> bool:
    """
    Helper function to check if a given set of edges forms a spanning tree.
    """
    if len(edges) != n - 1:
        return False

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    for u, v, _ in edges:
        union(u, v)

    root_set = {find(i) for i in range(n)}
    return len(root_set) == 1