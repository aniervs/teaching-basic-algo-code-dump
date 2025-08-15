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

def naive_knn(all_points, query_point, k):
    """
    Finds the k-nearest neighbors using a simple linear scan.
    """
    # Create list of (distance_sq, point) tuples
    distances = [(distance_sq(query_point, point), point) for point in all_points]
    
    # Sort by distance
    distances.sort(key=lambda x: x[0])
    
    # Return the first k points
    return [point for _, point in distances[:k]]

def verify_results(kdtree_results, naive_results, query_points):
    """Verify that both methods return the same results."""
    if not kdtree_results or not naive_results:
        return False, 0
    
    matches = 0
    for i in range(len(query_points)):
        # Sort both result sets by distance to query point for comparison
        kdtree_sorted = sorted(kdtree_results[i], key=lambda p: distance_sq(query_points[i], p))
        naive_sorted = sorted(naive_results[i], key=lambda p: distance_sq(query_points[i], p))
        
        # Check if the sets of points are the same
        if len(kdtree_sorted) == len(naive_sorted):
            all_match = True
            for j in range(len(kdtree_sorted)):
                # Compare distances with small tolerance for floating point precision
                kdtree_dist = distance_sq(query_points[i], kdtree_sorted[j])
                naive_dist = distance_sq(query_points[i], naive_sorted[j])
                if abs(kdtree_dist - naive_dist) > 1e-10:
                    all_match = False
                    break
            if all_match:
                matches += 1
    
    return matches == len(query_points), matches

def main():
    """Main function to run the performance comparison."""
    print(f"Generating {NUM_POINTS} random points in {DIM}D space...")
    points = generate_random_points(NUM_POINTS, DIM)
    query_points = generate_random_points(NUM_QUERIES, DIM)

    # --- KD-TREE PERFORMANCE TEST ---
    print("\n--- KD-Tree Performance Test ---")
    print("Building KD-Tree...")
    
    start_build = time.perf_counter()
    tree = KDTree(points)
    end_build = time.perf_counter()
    build_time_ms = (end_build - start_build) * 1000
    print(f"Build time: {build_time_ms:.2f} ms")

    kdtree_search_time_ms = 0
    kdtree_results = []
    
    if tree and tree.root:  # Check that tree was built successfully
        start_kdtree_search = time.perf_counter()
        for q_point in query_points:
            neighbors = tree.find_k_nearest_neighbors(q_point, K)
            kdtree_results.append(neighbors)
        end_kdtree_search = time.perf_counter()
        kdtree_search_time_ms = (end_kdtree_search - start_kdtree_search) * 1000
        print(f"KD-Tree search time for {NUM_QUERIES} queries: {kdtree_search_time_ms:.2f} ms")
    else:
        print("Error: KD-Tree was not built successfully!")
        return

    # --- NAIVE SEARCH PERFORMANCE TEST ---
    print("\n--- Naive Search Performance Test ---")
    naive_results = []
    
    start_naive_search = time.perf_counter()
    for q_point in query_points:
        neighbors = naive_knn(points, q_point, K)
        naive_results.append(neighbors)
    end_naive_search = time.perf_counter()
    naive_search_time_ms = (end_naive_search - start_naive_search) * 1000
    print(f"Naive search time for {NUM_QUERIES} queries: {naive_search_time_ms:.2f} ms")

    # --- ANALYSIS ---
    print("\n--- Analysis ---")
    if kdtree_search_time_ms > 0:
        speedup = naive_search_time_ms / kdtree_search_time_ms
        print(f"KD-Tree search was {speedup:.2f}x faster than naive search.")
        
        # Calculate theoretical complexity comparison
        theoretical_kdtree = NUM_QUERIES * K * (DIM ** 0.5) * (NUM_POINTS ** 0.5)  # Rough estimate
        theoretical_naive = NUM_QUERIES * NUM_POINTS
        theoretical_speedup = theoretical_naive / theoretical_kdtree if theoretical_kdtree > 0 else 0
        print(f"Theoretical speedup estimate: {theoretical_speedup:.2f}x")
    else:
        print("KD-Tree search time was too fast to measure accurately.")

    # --- VERIFICATION ---
    print("\n--- Verification ---")
    all_correct, matches = verify_results(kdtree_results, naive_results, query_points)
    
    print(f"Results match for {matches}/{len(query_points)} queries")
    if all_correct:
        print("✓ All results match! Both algorithms are working correctly.")
    else:
        print("✗ Some results don't match. Check your implementation.")
        # Show a sample mismatch for debugging
        for i in range(min(3, len(query_points))):
            if i < len(kdtree_results) and i < len(naive_results):
                kd_dists = [distance_sq(query_points[i], p) for p in kdtree_results[i]]
                naive_dists = [distance_sq(query_points[i], p) for p in naive_results[i]]
                print(f"Query {i}: KD-Tree distances: {sorted(kd_dists)[:3]}")
                print(f"Query {i}: Naive distances: {sorted(naive_dists)[:3]}")

    # --- SUMMARY ---
    print("\n--- Summary ---")
    print(f"Dataset: {NUM_POINTS} points in {DIM}D space")
    print(f"Queries: {NUM_QUERIES} queries for {K} nearest neighbors each")
    print(f"KD-Tree build time: {build_time_ms:.2f} ms")
    print(f"KD-Tree search time: {kdtree_search_time_ms:.2f} ms")
    print(f"Naive search time: {naive_search_time_ms:.2f} ms")
    print(f"Total KD-Tree time: {build_time_ms + kdtree_search_time_ms:.2f} ms")
    
    if kdtree_search_time_ms > 0:
        total_speedup = naive_search_time_ms / (build_time_ms + kdtree_search_time_ms)
        print(f"Overall speedup (including build time): {total_speedup:.2f}x")

if __name__ == "__main__":
    main()