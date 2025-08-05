class DisjointSet:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
    
    def find(self, u: int) -> int:
        """
        Finds the root of the set that u belongs to
        with path compression
        """
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, u: int, v: int) -> bool:
        """
        Unions the sets that u and v belong to
        """
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        self.parent[v_root] = u_root
        return True
        
    def connected(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)
