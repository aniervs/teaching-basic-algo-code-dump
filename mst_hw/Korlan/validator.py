from .disjoint_set import DisjointSet

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
    
    ### step 1. validate that the indices in mst_edges_idx are from 0 to len(edges_list) - 1
    for idx in mst_edges_idx:
        if idx < 0 or idx >= len(edges_list):
            return False
    
    ### step 2. validate that mst_edges_idx is a tree (...)
    if len(mst_edges_idx) != n - 1:
        return False
    
    # Extract the edges of the MST
    mst_edges = [edges_list[idx] for idx in mst_edges_idx]
    
    ds = DisjointSet(n)
    
    # Check if all edges in MST connect the graph without cycles
    for a, b, _ in mst_edges:
        if not ds.union(a, b):
            return False        # Cycle detected
    
    # Check if all nodes are connected
    root = ds.find(0)
    for i in range(1, n):
        if ds.find(i) != root:
            return False
    
    ### step 3. validate that it is a MST (each edge is optimal)
    
    # For each edge in MST, check if there's a better edge that can replace it
    # To do this, we'll temporarily remove each edge and see if a better edge exists
    
    # A set of edges in the MST for quick lookup
    mst_edge_set = set(mst_edges_idx)
    
    for edge_idx in mst_edges_idx:
        a, b, w = edges_list[edge_idx]
        
        # Temporarily remove this edge from the MST
        temp_mst_edges = [edges_list[idx] for idx in mst_edges_idx if idx != edge_idx]
        
        # Find the minimal edge that can reconnect the two components formed by removing (a, b)
        temp_ds = DisjointSet(n)
        
        for u, v, _ in temp_mst_edges:
            temp_ds.union(u, v)
        
        a_root = temp_ds.find(a)
        b_root = temp_ds.find(b)
        
        if a_root == b_root:
            continue  # No need to replace, but this shouldn't happen as we removed an edge
        
        # Look for the minimal edge in the original graph that connects a_root and b_root
        found_better = False
        for idx, (u, v, weight) in enumerate(edges_list):
            if idx in mst_edge_set and idx != edge_idx:
                continue  # Skip edges already in MST (except the one we removed)
            u_root = temp_ds.find(u)
            v_root = temp_ds.find(v)
            if u_root != v_root:
                if weight < w:
                    found_better = True
                    break
        
        if found_better:
            return False
    
    return True


def run_comprehensive_tests():
    """
    Test the MST validator with various cases
    """
    print("=== MST Validator Tests (Path Maximum Property) ===\n")
    
    test_cases = [
        {
            "name": "Simple Valid MST",
            "n": 4,
            "edges": [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10), (1, 3, 8)],
            "mst_indices": [0, 1, 2],  # weights: 1, 2, 3
            "expected": True,
            "explanation": "MST with weights 1,2,3. Non-MST edges (0,3,10) and (1,3,8) are heavier than path maximums."
        },
        
        {
            "name": "Invalid MST - Suboptimal Choice",
            "n": 4,
            "edges": [(0, 1, 1), (1, 2, 2), (2, 3, 3), (0, 3, 10), (1, 3, 4)],
            "mst_indices": [0, 1, 3],  # Uses (0,3,10) instead of (2,3,3)
            "expected": False,
            "explanation": "Uses edge (0,3,10) when (2,3,3) is available and lighter than path max."
        },
        
        {
            "name": "Valid MST - Multiple Equal Options",
            "n": 4,
            "edges": [(0, 1, 5), (1, 2, 5), (2, 3, 5), (0, 3, 5), (1, 3, 5), (0, 2, 5)],
            "mst_indices": [0, 1, 2],  # All weights are 5
            "expected": True,
            "explanation": "All edges have equal weight, so any spanning tree is minimal."
        },
        
        {
            "name": "Invalid - Creates Cycle",
            "n": 3,
            "edges": [(0, 1, 1), (1, 2, 2), (0, 2, 3)],
            "mst_indices": [0, 1, 2],  # All 3 edges
            "expected": False,
            "explanation": "Has 3 edges for 3 nodes, creates a cycle."
        },
        
        {
            "name": "Invalid - Disconnected",
            "n": 4,
            "edges": [(0, 1, 1), (2, 3, 2), (0, 2, 10)],
            "mst_indices": [0, 1],  # Missing connection
            "expected": False,
            "explanation": "Two components not connected."
        },
        
        {
            "name": "Single Node",
            "n": 1,
            "edges": [],
            "mst_indices": [],
            "expected": True,
            "explanation": "Single node requires no edges."
        },
        
        {
            "name": "Two Nodes",
            "n": 2,
            "edges": [(0, 1, 5)],
            "mst_indices": [0],
            "expected": True,
            "explanation": "Two nodes connected by single edge."
        },
        
        {
            "name": "Path Property Violation",
            "n": 4,
            "edges": [(0, 1, 1), (1, 2, 10), (2, 3, 1), (0, 3, 5)],
            "mst_indices": [0, 1, 2],  # Path 0->1->2 has max weight 10, but (0,3) has weight 5 < 10
            "expected": False,
            "explanation": "Non-MST edge (0,3,5) is lighter than heaviest edge (1,2,10) on path 0->1->2->3."
        }
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['name']}")
        print(f"  Description: {test['explanation']}")
        
        try:
            result = validate_mst(test["n"], test["edges"], test["mst_indices"])
            status = "PASS" if result == test["expected"] else "FAIL"
            
            print(f"  Result: {status} (Expected: {test['expected']}, Got: {result})")
            
            if status == "PASS":
                passed += 1
            else:
                print(f"  Graph: n={test['n']}, edges={test['edges']}")
                print(f"  MST indices: {test['mst_indices']}")
                
        except Exception as e:
            print(f"  Result: ERROR - {e}")
        
        print()
    
    print(f"Final Results: {passed}/{total} tests passed")
    
    # Demonstrate the path property with a specific example
    print("\n=== Path Property Demonstration ===")
    n = 4
    edges = [(0, 1, 1), (1, 2, 10), (2, 3, 1), (0, 3, 5)]
    mst_indices = [0, 1, 2]  # This should be invalid
    
    print(f"Graph: n={n}, edges={edges}")
    print(f"Proposed MST indices: {mst_indices}")
    print(f"MST edges: {[edges[i] for i in mst_indices]}")
    print(f"Non-MST edge: {edges[3]} (index 3)")
    print(f"Path from 0 to 3 in MST: 0 -> 1 (weight 1) -> 2 (weight 10) -> 3 (weight 1)")
    print(f"Maximum weight on path: 10")
    print(f"Non-MST edge weight: 5")
    print(f"Since 5 < 10, we could replace edge (1,2,10) with (0,3,5) to get a lighter spanning tree.")
    print(f"Therefore, this MST is invalid.")
    
    result = validate_mst(n, edges, mst_indices)
    print(f"Validator result: {result}")


if __name__ == "__main__":
    run_comprehensive_tests()