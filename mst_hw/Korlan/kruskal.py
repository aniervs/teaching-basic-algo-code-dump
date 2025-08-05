from .disjoint_set import DisjointSet
from .generator import generator, random
from .validator import validate_mst

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
    sorted_edges = sorted(enumerate(edges_list), key=lambda x: x[1][2])
    ds = DisjointSet(n)
    mst_indices = []
    
    for idx, (u, v, weight) in sorted_edges:
        if ds.union(u, v):
            mst_indices.append(idx)
            if len(mst_indices) == n - 1:
                break
    
    return mst_indices

def stress_test():
    random.seed(42)
    test_cases = 10
    for _ in range(test_cases):
        n = random.randint(1, 20)
        p = random.uniform(0.3, 0.8)
        edges = generator(n, p)
        mst_indices = kruskal(n, edges)
        is_valid = validate_mst(n, edges, mst_indices)
        print(f"Test case with n={n}, p={p:.2f}: {'Valid' if is_valid else 'Invalid'} MST")
        if not is_valid:
            print("Invalid MST found!")
            break
     
     
if __name__ == "__main__":   
    stress_test()