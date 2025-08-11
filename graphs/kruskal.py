class DisjointSets:
    def __init__(self, n: int):
        """
        starting n sets of size 1 each
        """
        self.id = [i for i in range(n)]  # id[a] = a for every a from 0 to n - 1
        self.sets = [[i] for i in range(n)] # every element has its own set
        
        
    def check(self, a: int, b: int) -> bool:
        return self.id[a] == self.id[b]
    
    def join(self, a: int, b: int):
        """
        we want to take the set where a is and the set where b is and merge them into a single set
        """
        ia = self.id[a]
        ib = self.id[b]
        if ia == ib: # they're already in the same set, so we don't do anything
            return 
        # otherwise, they have be merged
        if len(self.sets[ia]) < len(self.sets[ib]):
            # go through every element of ia and update their ids to ib 
            for e in self.sets[ia]:
                self.id[e] = ib 
            # merge ia into ib 
            self.sets[ib].extend(self.sets[ia])
            self.sets[ia].clear()
        else:
            # go through every element of ib and update their ids to ia 
            for e in self.sets[ib]:
                self.id[e] = ia 
            # merge ib into ia         
            self.sets[ia].extend(self.sets[ib])
            self.sets[ib].clear()
        

def kruskal(n: int, edges_list: list[tuple[int,int,int]]) -> list[tuple[int,int,int]]:
    """
    n: number of nodes (nodes are indexed from 0 to n - 1)
    edges_list: every edge is a tuple (a, b, weight)
    
    return: a list of edges in the Minimum Spanning Tree
    """
    # step 1. sort the edges in increasing order of weight 
    edges_list.sort(key = lambda edge: edge[2]) # O(m * log (m)) time 
    # step 2. initialize the Disjoint Sets data structures 
    ds = DisjointSets(n)
    
    mst_edges = []
    # step 3. go through every edge in increasing order
    for a, b, weight in edges_list:
        # join a and b if it's possible (if a and b are in different connected components/ sets)
        if ds.check(a, b): # if they're already in the same connected component
            continue 
        ds.join(a, b)
        mst_edges.append((a, b, weight))
        if len(mst_edges) == n - 1: # early stopping
            break

    if len(mst_edges) < n - 1:
        raise AssertionError('the graph is not connected, hence we cannot find a minimum spanning TREE')
    if len(mst_edges) > n - 1:
        raise AssertionError('the MST algorithm went wrong')
    
    return mst_edges
        
def main():
    n_nodes = 8
    edges_list = [
        (0, 2, 30),
        (0, 4, 1),
        (0, 3, 4),
        (0, 5, 100),
        (1, 4, 5),
        (2, 5, 2),
        (3, 4, 3),
        (3, 5, 1),
        (3, 7, 2),
        (3, 6, 4)
    ]
    
    mst = kruskal(n_nodes, edges_list)
    for a, b, w in mst:
        print(a, b, w)
    

if __name__ == '__main__':
    main()

