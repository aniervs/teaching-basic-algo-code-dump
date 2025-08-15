from generator import generator
from validator import validate_mst
from prim import prim_n2, prim_mlogn
from kruskal import kruskal

def main(num_tests=100, n = 50, p=0.5):
    """
    Main function to run the tests for MST algorithms.

    Args:
        num_tests (int): Number of tests to run.
        n (int): Number of vertices in the graph.
        p (float): Probability of edge creation between any two vertices.
    """

    for _ in range(num_tests):
        edges = generator(n, p) # Generate a random graph
        mst_kruskal = kruskal(n, edges) # Run kruskal
        mst_prim_n2 = prim_n2(n, edges) # Run prim
        mst_prim_mlogn = prim_mlogn(n, edges) 
        # validate
        assert validate_mst(n, edges, mst_kruskal), "Kruskal's MST validation failed"
        assert validate_mst(n, edges, mst_prim_n2), "Prim's (O(n^2)) MST validation failed"
        assert validate_mst(n, edges, mst_prim_mlogn), "Prim's (O(m * log n)) MST validation failed"

    print(f"All {num_tests} tests passed successfully!")

if __name__ == '__main__':
    main()