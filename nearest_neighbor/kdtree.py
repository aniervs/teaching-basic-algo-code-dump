import heapq

class KDTree:
    """A Python implementation of a KD-Tree."""

    # Internal class for a single node in the tree
    class Node:
        def __init__(self, point=None, axis=None, left=None, right=None):
            self.point = point
            self.axis = axis
            self.left = left
            self.right = right

    def __init__(self, points):
        """Initializes the KD-Tree by building it from a list of points."""
        self.dim = len(points[0]) if points else 0
        self.root = self._build(points, 0)

    @staticmethod
    def _distance_sq(p1, p2):
        """Calculates the squared Euclidean distance between two points."""
        return sum([(a - b) ** 2 for a, b in zip(p1, p2)])

    # ------------------------------------------------------------------
    # TODO: IMPLEMENT THE FOLLOWING TWO METHODS
    # ------------------------------------------------------------------

    def _build(self, points, depth):
        """
        Recursively builds the KD-Tree.

        Args:
            points (list): A list of points for this subtree.
            depth (int): The current depth in the tree.

        Returns:
            Node: The root node of the constructed subtree.
        
        **Implementation Steps:**
        1.  Handle the base case: If `points` is empty, return `None`.
        2.  Determine the splitting axis using `depth % self.dim`.
        3.  Sort the points along the splitting axis.
        4.  Find the median index. The point at this index will be the current node's point.
        5.  Create a new `Node` with the median point and the current axis.
        6.  Recursively call `_build` to create the left and right children.
            - The left child will be built from points before the median.
            - The right child will be built from points after the median.
        """
        if not points:
            return None

        # --- YOUR IMPLEMENTATION HERE ---

        return None # Placeholder

    def _knn_search(self, node, query_point, k, neighbors):
        """
        Recursively searches for the k-nearest neighbors.

        Args:
            node (Node): The current node in the KD-Tree.
            query_point (list): The point for which we are finding neighbors.
            k (int): The number of neighbors to find.
            neighbors (list): A min-heap to keep track of the k-nearest neighbors.
                              It stores tuples of (-distance_sq, point).
        
        **Implementation Steps:**
        1.  Handle the base case: If `node` is `None`, return.
        2.  Calculate the squared distance from the current node's point to the `query_point`.
        3.  Update the `neighbors` heap. If the heap has fewer than `k` items, or if the current
            point is closer than the farthest point in the heap, update the heap.
            - Remember `heapq` is a min-heap. To find the "farthest" neighbor (which has the
              largest distance), you'll look at `neighbors[0]`.
            - You are storing negative distances, so the "smallest" item in the heap
              (at `neighbors[0]`) corresponds to the largest distance.
        4.  Determine which subtree to search first (the "near" side) based on the `query_point`'s
            value along the node's splitting axis.
        5.  Recursively search the "near" side.
        6.  **Backtracking/Pruning Step**: Check if the "far" side needs to be searched. You only
            need to search the other side if the squared distance from the `query_point` to the
            splitting plane is less than the squared distance to the farthest neighbor found so far.
        7.  If the condition in step 6 is met, recursively search the "far" side.
        """
        if node is None:
            return

        # --- YOUR IMPLEMENTATION HERE ---
        pass

    # ------------------------------------------------------------------
    # PUBLIC METHOD (PROVIDED)
    # ------------------------------------------------------------------

    def find_k_nearest_neighbors(self, query_point, k):
        """
        Finds the k-nearest neighbors to a query point.
        This is the public method that users will call.
        """
        if self.root is None or k == 0:
            return []
            
        # We use a min-heap to store (-distance_sq, point) tuples.
        # Storing negative distances simulates a max-heap, making it easy
        # to find and replace the farthest neighbor.
        neighbors = [] 

        self._knn_search(self.root, query_point, k, neighbors)
        
        # The result is a list of points, sorted from nearest to farthest.
        neighbors.sort(key=lambda x: -x[0]) # Sort by distance
        return [point for neg_dist, point in neighbors]