import matplotlib.pyplot as plt
import pandas as pd
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
    distance_between_points = [(distance_sq(point, query_point), point) for point in all_points]
    distance_between_points.sort(key=lambda x: x[0])
    return [point for dist, point in distance_between_points[:k]]


def run(dim=DIM, n_points=NUM_POINTS, n_queries=NUM_QUERIES, k=K, seed=42):
    """Main function to run the performance comparison."""
    random.seed(seed)
    print(f"Generating {n_points} random points in {dim}D space...")
    points = generate_random_points(n_points, dim)
    query_points = generate_random_points(n_queries, dim)

    # --- KD-TREE PERFORMANCE TEST ---
    print("\n--- KD-Tree Performance Test ---")
    print("Building KD-Tree...")
    
    start_build = time.perf_counter()
    tree = KDTree(points)  # Build the tree
    end_build = time.perf_counter()
    build_time_ms = (end_build - start_build) * 1000
    print(f"Build time: {build_time_ms:.2f} ms")

    kdtree_search_time_ms = 0
    kd_results = []
    start_kdtree_search = time.perf_counter()
    for q_point in query_points:
        neighbors = tree.find_k_nearest_neighbors(q_point, k)
        kd_results.append(neighbors)
    end_kdtree_search = time.perf_counter()
    kdtree_search_time_ms = (end_kdtree_search - start_kdtree_search) * 1000
    print(f"KD-Tree search time for {n_queries} queries: {kdtree_search_time_ms:.2f} ms")

    # --- NAIVE SEARCH PERFORMANCE TEST ---
    print("\n--- Naive Search Performance Test ---")
    start_naive_search = time.perf_counter()
    naive_results = []
    for q_point in query_points:
        neighbors = naive_knn(points, q_point, k)
        naive_results.append(neighbors)
    end_naive_search = time.perf_counter()
    naive_search_time_ms = (end_naive_search - start_naive_search) * 1000
    print(f"Naive search time for {n_queries} queries: {naive_search_time_ms:.2f} ms")

    # --- ANALYSIS ---
    print("\n--- Analysis ---")
    speedup = naive_search_time_ms / kdtree_search_time_ms if kdtree_search_time_ms > 0 else float("inf")
    print(f"KD-Tree search was {speedup:.2f} times faster than naive search.")
    
    # Verify results
    print("\nVerifying KD-Tree results vs Naive results...")
    mismatches = 0
    for q_point, kd_res, naive_res in zip(query_points, kd_results, naive_results):
        kd_sorted = sorted(kd_res, key=lambda p: distance_sq(p, q_point))
        naive_sorted = sorted(naive_res, key=lambda p: distance_sq(p, q_point))
        if kd_sorted != naive_sorted:
            mismatches += 1
    print(f"Found {mismatches} mismatches out of {n_queries} queries")
    
    return {
        "build_ms": build_time_ms,
        "kdtree_ms": kdtree_search_time_ms,
        "naive_ms": naive_search_time_ms,
        "speedup": speedup,
        "mismatches": mismatches,
    }


def experiment_vary_n(dim=2, k=5, n_values=None):
    if n_values is None:
        n_values = [1_000, 5_000, 10_000, 20_000, 50_000, 100_000]
    rows = []
    for n in n_values:
        res = run(dim=dim, n_points=n, n_queries=100, k=k, seed=123)
        rows.append({"N": n, **res})
    df = pd.DataFrame(rows)
    return df

def experiment_vary_dim(n_points=50_000, k=5, dims=None):
    if dims is None:
        dims = [2, 4, 8, 12, 16, 20]
    rows = []
    for d in dims:
        res = run(dim=d, n_points=n_points, n_queries=100, k=k, seed=456)
        rows.append({"DIM": d, **res})
    df = pd.DataFrame(rows)
    return df

def experiment_vary_k(n_points=50_000, dim=2, ks=None):
    if ks is None:
        ks = [1, 2, 5, 10, 20, 50]
    rows = []
    for k in ks:
        res = run(dim=dim, n_points=n_points, n_queries=100, k=k, seed=789)
        rows.append({"K": k, **res})
    df = pd.DataFrame(rows)
    return df

def main():
    # A base case
    # base_results = run(dim=DIM, n_points=NUM_POINTS, n_queries=NUM_QUERIES, k=K, seed=42)

    # Run experiments
    df_n = experiment_vary_n(dim=2, k=5)
    df_d = experiment_vary_dim(n_points=50_000, k=5)
    df_k = experiment_vary_k(n_points=50_000, dim=2)
    path = "C:/Users/Kora/Dev/teaching-basic-algo-code-dump/nearest_neighbor/Korlan/"
    
    """
    2. How does the performance gap change as you increase the NUM_POINTS? Why?
    Make some plots of that (performance gap vs NUM_POINTS)
    
    Answer: KD-Tree search time grows logarithmically with NUM_POINTS (O(log N)),
    while naive search time grows linearly (O(N)). So, the speedup increases as NUM_POINTS grows larger.
    """
    plt.figure()
    plt.plot(df_n["N"], df_n["naive_ms"], label="Naive (ms)")
    plt.plot(df_n["N"], df_n["kdtree_ms"], label="KD-Tree (ms)")
    plt.xlabel("Number of points (N)")
    plt.ylabel("Total query time (ms)")
    plt.title("Query Time vs N (100 queries, dim=2, k=5)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path +"/query_time_vs_N.png")
    plt.show()

    plt.figure()
    plt.plot(df_n["N"], df_n["speedup"])
    plt.xlabel("Number of points (N)")
    plt.ylabel("Speedup (Naive / KD-Tree)")
    plt.title("Speedup vs N")
    plt.tight_layout()
    plt.savefig(path + "/speedup_vs_N.png")
    plt.show()
    
    """
    3. How does the performance change as you increase the DIM? (e.g., to 10 or 20)?
    This phenomenon is known as the 'Curse of Dimensionality'. Briefly explain why this happens."
    
    Answer: In higher dimensions, starting from DIM=8, the performance change of KD-Tree search time is growing polynomially,
    reaching almost the same performance as naive search time for DIM=20.
    Possible reasons of the 'Curse of Dimensionality':
    - The pruning becomes more time-consuming - more subtrees need to be searched;
    - The tree depth increases, reducing the benefit of partitioning;
    - In high dimensions, all points tend to be almost equally far apart due to the vastness of the space.
    So, the data points spread out far apart from each other.
    """
    plt.figure()
    plt.plot(df_d["DIM"], df_d["naive_ms"], label="Naive (ms)")
    plt.plot(df_d["DIM"], df_d["kdtree_ms"], label="KD-Tree (ms)")
    plt.xlabel("Dimensionality (D)")
    plt.ylabel("Total query time (ms)")
    plt.title("Query Time vs Dimensionality (N=50_000, k=5, 100 queries)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path + "/query_time_vs_dim.png")
    plt.show()
    
    """
    4. How does increasing 'K' affect the performance of each method? Also make some plots.
    
    Answer:
    For KD-tree, the query time stays almost flat as K increases from 1 to 50.
    It may mean that retrieving more neighbors doesn't add much overhead compared to the traversal itself.
    
    For the naive search, the query time grows slightly with K.
    It may mean that retrieving more neighbors requires O(K) time and extra allocations.
    """
    plt.figure()
    plt.plot(df_k["K"], df_k["naive_ms"], label="Naive (ms)")
    plt.plot(df_k["K"], df_k["kdtree_ms"], label="KD-Tree (ms)")
    plt.xlabel("K (neighbors)")
    plt.ylabel("Total query time (ms)")
    plt.title("Query Time vs K (N=50_000, dim=2, 100 queries)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(path + "/query_time_vs_K.png")
    plt.show()

if __name__ == "__main__":
    main()