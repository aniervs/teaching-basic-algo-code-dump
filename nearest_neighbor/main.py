import random
import time
from kdtree import KDTree # Make sure kdtree.py is in the same directory

# --- STRESS TEST PARAMETERS ---
DIM = 2
NUM_POINTS = 100_000
NUM_QUERIES = 100
K = 5

def generate_random_points(n, dim, min_val=0.0, max_val=1000.0):
    """Generates a list of n random points in dim dimensions."""
    return [[random.uniform(min_val, max_val) for _ in range(dim)] for _ in range(n)]

def distance_sq(p1, p2):
    """Calculates the squared Euclidean distance between two points."""
    return sum([(a - b) ** 2 for a, b in zip(p1, p2)])

# ------------------------------------------------------------------
# TODO: IMPLEMENT THE FOLLOWING FUNCTION
# ------------------------------------------------------------------

def naive_knn(all_points, query_point, k):
    """
    Finds the k-nearest neighbors using a simple linear scan.

    **Implementation Steps:**
    1.  Create a list of `(distance_sq, point)` tuples for every point in `all_points`.
    2.  Sort this list based on the distances.
    3.  Return the points from the first `k` tuples in the sorted list.
    """
    # --- YOUR IMPLEMENTATION HERE ---
    return [] # Placeholder


def main():
    """Main function to run the performance comparison."""
    print(f"Generating {NUM_POINTS} random points in {DIM}D space...")
    points = generate_random_points(NUM_POINTS, DIM)
    query_points = generate_random_points(NUM_QUERIES, DIM)

    # --- KD-TREE PERFORMANCE TEST ---
    print("\n--- KD-Tree Performance Test ---")
    print("Building KD-Tree...")
    
    start_build = time.perf_counter()
    # TODO: Instantiate your KDTree with the generated points.
    # tree = KDTree(points)
    end_build = time.perf_counter()
    build_time_ms = (end_build - start_build) * 1000
    print(f"Build time: {build_time_ms:.2f} ms")

    # This is a placeholder for the tree variable
    tree = None 

    kdtree_search_time_ms = 0
    if tree:
        start_kdtree_search = time.perf_counter()
        for q_point in query_points:
            # TODO: Call your KD-Tree's find_k_nearest_neighbors function.
            # neighbors = tree.find_k_nearest_neighbors(q_point, K)
            pass # Placeholder
        end_kdtree_search = time.perf_counter()
        kdtree_search_time_ms = (end_kdtree_search - start_kdtree_search) * 1000
        print(f"KD-Tree search time for {NUM_QUERIES} queries: {kdtree_search_time_ms:.2f} ms")


    # --- NAIVE SEARCH PERFORMANCE TEST ---
    print("\n--- Naive Search Performance Test ---")
    start_naive_search = time.perf_counter()
    for q_point in query_points:
        # TODO: Call your naive_knn function.
        # neighbors = naive_knn(points, q_point, K)
        pass # Placeholder
    end_naive_search = time.perf_counter()
    naive_search_time_ms = (end_naive_search - start_naive_search) * 1000
    print(f"Naive search time for {NUM_QUERIES} queries: {naive_search_time_ms:.2f} ms")


    # --- ANALYSIS ---
    print("\n--- Analysis ---")
    if kdtree_search_time_ms > 0:
        speedup = naive_search_time_ms / kdtree_search_time_ms
        print(f"KD-Tree search was {speedup:.2f} times faster than naive search.")
    
    #TODO:
    # 1. Verify that both KD-tree and the naive search provide the same set of points (you may need to sort them to compare).
    # 2. How does the performance gap change as you increase the NUM_POINTS? Why? Make some plots of that (performance gap vs NUM_POINTS)
    # 3. How does the performance change as you increase the DIM? (e.g., to 10 or 20)? This phenomenon is known as the 'Curse of Dimensionality'. Briefly explain why this happens."
    # 4. How does increasing 'K' affect the performance of each method?" Also make some plots.

if __name__ == "__main__":
    main()