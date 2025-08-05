from .generator import generator, random
from .validator import validate_mst
from .prim import prim_n2, prim_mlogn
from .kruskal import kruskal

def calculate_weight(edges, mst_indices):
    """Calculate total weight of MST"""
    return sum(edges[idx][2] for idx in mst_indices)

def main():
    # This function should stress test all implemented algorithms
    # repeat many times...
    # 1. generate a random graph
    # 2. run kruskal and prim
    # 3. validate the results
    # 4. if the validator returns false, raise an assertion
    test_cases = 10
    max_vertices = 100
    for test_num in range(1, test_cases + 1):
        # Generate initial random graph
        n = random.randint(2, max_vertices)
        p = random.uniform(0.3, 0.8)
        edges = generator(n, p)
        
        algorithms = [
            ("Prim O(n^2)", prim_n2),
            ("Prim O(m log n)", prim_mlogn),
            ("Kruskal", kruskal)
        ]
        
        reference_mst = None
        for name, algorithm in algorithms:
            mst_indices = algorithm(n, edges)
            if not validate_mst(n, edges, mst_indices):
                print(f"\nTest case {test_num} failed with {name}!")
                print(f"Graph: n={n}, edges={edges}")
                print(f"Invalid MST: {mst_indices}")
                raise AssertionError(f"{name} produced invalid MST")
            
            # Set first valid MST as reference
            if reference_mst is None:
                reference_mst = mst_indices
            elif calculate_weight(edges, mst_indices) != calculate_weight(edges, reference_mst):
                print(f"\nTest case {test_num}: MST weight mismatch with {name}!")
                raise AssertionError("MST weight mismatch between algorithms")

if __name__ == '__main__':
    main()