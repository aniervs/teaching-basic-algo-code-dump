### Task 7

In both cases we could improve sorting time by applying counting sort. I would use a hashmap, or simply an array with $n$ or $W$ indices (where index stands for a value from $1$ to $n$ or $W$) of tuples (u, v, weight).

In the first case (weights from $1$ to $n$), counting sort takes $O(m + n)$ time. For Kruskal algorithm, with path compression and union by rank, each operation is nearly constant time - $O(\alpha(n))$, where $\alpha(n)$ is the inverse Ackermann function, $n$ - number of nodes, $m$ - number of edges. This could lead to a complexity of $O(m + n + m \alpha(n)) = O(m \alpha(n))$.

In the second case (constant $W$) - the idea is the same. Counting sort takes $O(m + W) = O(m)$ time because $W$ is a constant. The union-find operations take $O(m \alpha(n))$ time. The total time complexity is $O(m + m \alpha(n)) = O(m \alpha(n))$.

### Task 8

Instead of using a heap or a linear search to find the minimal non-MST node from the currently processed node $u$, we can use an array of lists of nodes: (e.g.: ```buckets = [[] for _ in range(n + 1)]```), where the index stands for the weight in the range from $1$ to $n$ (or $W$), and the value is a list of nodes with $minimal_edge = w$.

We could track the next unprocessed minimal node during relaxation by updating some global minimal_bucket. At the same time, if we update a weight, we need to remove the node from the buckets list:

```
if not in_mst[v] and weight < key[v]: // Relaxation
    buckets[min_edge[v]].remove(v)
```

This requires scanning the entire bucket to find $v$, making it $O(k)$ (where $k$ - number of elements in the bucket).

We can optimize the buckets data structure by using the doubly linked list (DLL) and having a hashmap that stores the pointer to the specific DLL node for each vertex $v$. Then, deleting a node from DLL will take $O(1)$.

Example:

Bucket[w]: [A <-> B <-> C]  
Remove B: update A.next = C and C.prev = A (no scanning needed).

Pseudo-code:

```
min_edge = [inf] * n
in_mst = [False] * n
buckets = [DoublyLinkedList() for _ in range(n + 1)]  // Weights are 1..n
    
// Start with node 0
min_edge[0] = 0
// node_ptr acts like a hashmap, letting to jump directly to v’s node in its bucket.
node_ptr[0] = buckets[0].append(0) 

min_bucket = 0	// the smallest non-empty bucket
    
while min_bucket <= n:
    // Find the next vertex to add to MST (O(1) due to min_bucket tracking)
    if not buckets[min_bucket]:
        min_bucket += 1
        continue
        
    u = buckets[min_bucket].pop()
        
    if in_mst[u]:
        continue  // Skip if already in MST
        
    in_mst[u] = True
        
    // Relax all edges (u, v)
    for (v, weight) in G.adjacent_edges(u):
        if not in_mst[v] and weight < key[v]:
            // Remove v from old bucket (if previously assigned)
            if min_edge[v] <= n:
                buckets[min_edge[v]].remove(node_ptr[v]) // O(1) 
                
                // Update key and add to new bucket
                key[v] = weight
                parent[v] = u
                node_ptr[v] = buckets[weight].append(v)  // O(1)
                
                // Update min_bucket if necessary
                if weight < min_bucket:
                    min_bucket = weight
```

Total time complexity for both cases: $O(n + m)$.
