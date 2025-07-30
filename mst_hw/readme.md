# Minimum Spanning Tree Homework

This homework is about Minimum Spanning Trees. You will get to implement different algorithms and test them. There's also some theoretical questions that must be answered; some of them do ask to implement some extra functionalities; in those cases, create a new module with the corresponding new functions.


## Task 1.
Implement a test case generator that generates connected graphs. You can get inspiration from the attached code. This generator should have two parameters:

- $n$: the number of nodes in the graph to be generated
- $p$: the probability of adding each edge.

The way the generator works is that it will include each edge with probability $p$, and it will exclude each edge with probability $1 - p$.

That means that in average, the number of edges of the graph will be $p \cdot \frac{n \cdot (n-1)}{2}. Hence, $p$ controls the density of the graph: the bigger $p$, the denser the graph. For example, if $p = 0.75$, you expect the graph to have around $3/4$ of all possible edges, that is $\frac{3\cdot n(n-1)}8$ edges. But if $p = 0.2$, then you expect the graph to have $1/5$ of all possible edges, that is $\frac{n(n-1)}{10}$ edges.

##  Task 2.
Implement a validator for the MST algorithms. That is, a function that receives a graph (given by the number of nodes and the list of edges) and another graph (given by the list of indices of the edges of the original graph), that indicates the MST found by any of the algorithms. The validator should check:
-  that the given MST is actually a tree (by checking that it has exactly $n$ nodes and $n-1$ edges and it's connected)
- that the given MST is actually spanning tree (the edges it has are actual edges from the original graph)
- that the given MST is actually a minimum spanning tree. How to check that? Well, you have to check that every edge in the given MST is optimal, in the sense that removing it, and replacing it by another edge, will produce a spanning tree that isn't better than the current one.

## Task 3. 
Implement Prim's algorithm in $O(n^2)$ time, without priority queue. Stress-test it with the generator and validator from previous tasks.

## Task 4.
Implement Prim's algorithm in $O(m \cdot \log n)$ time with priority queue. Stress-test it with the generator and validator from previous tasks.

## Task 5.
Implement Kruskal's algorithm in $O(m \cdot \log n)$ with the Disjoint Sets data structure. Stress-test it with the generator and validator from previous tasks.

## Task 6.
Run some tests to measure the efficiency of these algorithms.
- Go through different values of $n$ (the number of nodes) and generate many graphs of each size.
- Run the algorithms on all those graphs, and measure the average running time per graph size.
- Plot the running time (in milliseconds) of all the algorithms vs the graph size.
- To consider for better benchmarking: fixing different values of $p$ (density of the graph), and also plotting the average running time per density.


## Task 7.
Suppose that all edge weights in a graph of $n$ nodes are integers in the range from $1$ to $n$. How fast can you make Kruskal's algorithm run? What if the edge weights are integers in the range from $1$ to $W$ for some constant $W$?

## Task 8.
Suppose that all edge weights in a graph of $n$ nodes are integers in the range from $1$ to $n$. How fast can you make Prim's algorithm run? What if the edge weights are integers in the range from $1$ to $W$ for some constant $W$?

## Task 9.
Suppose that a graph has a minimum spanning tree already computed. How
quickly can you update the minimum spanning tree upon adding a new vertex $v$ and incident edges to $v$ to this graph? Implement this new function `add_vertex(n: int, graph: list[tuple[int,int,int]], mst: list[int], new_incident_edges: list[tuple[int,int]])`, that will add a new vertex (with label $n$) and the edges between that vertex and the ones listed in `new_incident_edges` to the graph, and update the MST.

## Task 10.
Suppose that a graph has a minimum spanning tree already computed. How
quickly can you update the minimum spanning tree upon adding a new edge between already-existing vertices? This new edge generates a cycle, and it could potentially be part of the MST. Implement this new function `add_edge(n: int, graph: list[tuple[int,int,int]], mst: list[int], new_edge: tuple[int,int,int])`, that will add a new edge to the graph, and it will update the MST.