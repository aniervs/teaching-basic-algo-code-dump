from .generator import generator
from .prim import prim_n2, prim_mlogn
from .kruskal import kruskal

import matplotlib.pyplot as plt
import time
from tqdm import tqdm

def measure_time(algorithm: callable, n: int, edges_list: list[tuple[int,int,int]]) -> float:
    """
    Measures the running time of a given algorithm in milliseconds
    """
    start_time = time.time()
    algorithm(n, edges_list)
    end_time = time.time()
    return (end_time - start_time) * 1000

def main():
    # This function should measure the efficiency of implemented algorithms
    # go through different values of n (eg: 10, 100, 1000, 10000) and for each n:
    # repeat >= 10 times:
    # 1. generate  random graph of size n
    # 2. run kruskal and prim on all those graphs
    # 3. measure the running time and average each (prim's and kruskal's)
    # 4. plot the results of running time vs n. There should be three curves:
    #       one for Kruskal, one for Prim's in O(n^2), and one for Prim's in O(m \log n)
    
    # additional:
    # vary the density and perform similar tests
    
    # USE tqdm to have a progress bar for the different graphs
    
    n_values = [10, 100, 500, 1000]  # graph sizes
    p_values = [0.2, 0.5, 0.8]       # densities
    repeats = 10                     # number of repetitions per size and density

    results = {
        'kruskal': {n: {p: [] for p in p_values} for n in n_values},
        'prim_n2': {n: {p: [] for p in p_values} for n in n_values},
        'prim_mlogn': {n: {p: [] for p in p_values} for n in n_values}
    }

    for n in tqdm(n_values, desc="Graph Sizes"):
        for p in tqdm(p_values, desc="Densities", leave=False):
            for _ in range(repeats):
                edges = generator(n, p)
                
                # Measure Kruskal's algorithm
                kruskal_time = measure_time(kruskal, n, edges)
                results['kruskal'][n][p].append(kruskal_time)
                
                # Measure Prim's O(n^2) algorithm
                prim_n2_time = measure_time(prim_n2, n, edges)
                results['prim_n2'][n][p].append(prim_n2_time)
                
                # Measure Prim's O(m*log(n)) algorithm
                prim_mlogn_time = measure_time(prim_mlogn, n, edges)
                results['prim_mlogn'][n][p].append(prim_mlogn_time)

    # Calculate average times for each algorithm
    avg_times = {
        'kruskal': {n: {p: sum(results['kruskal'][n][p]) / repeats for p in p_values} for n in n_values},
        'prim_n2': {n: {p: sum(results['prim_n2'][n][p]) / repeats for p in p_values} for n in n_values},
        'prim_mlogn': {n: {p: sum(results['prim_mlogn'][n][p]) / repeats for p in p_values} for n in n_values}
    }

    # Plot the results
    plt.figure(figsize=(12, 8))
    for p in p_values:
        plt.plot(n_values, [avg_times['kruskal'][n][p] for n in n_values], label=f'Kruskal p={p}', marker='o')
        plt.plot(n_values, [avg_times['prim_n2'][n][p] for n in n_values], label=f'Prim O(n^2) p={p}', marker='s')
        plt.plot(n_values, [avg_times['prim_mlogn'][n][p] for n in n_values], label=f'Prim O(m log n) p={p}', marker='^')
    
    plt.xlabel('Number of Nodes (n)')
    plt.ylabel('Average Running Time (ms)')
    plt.title('Performance of MST Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()