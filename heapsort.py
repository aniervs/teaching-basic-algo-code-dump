class Heap:
    def __init__(self):
        self._lst = [] # this list contains the values of each node 
    
    @staticmethod
    def _parent(u: int) -> int:
        # this is the integer division (which in postive numbers means rounding down)
        return (u - 1) // 2

    @staticmethod
    def _left(u: int) -> int:
        return 2 * u + 1 
    
    @staticmethod
    def _right(u: int) -> int:
        return 2 * u + 2     
        
    def heapify_up(self, node: int):
        while node != 0 and self._lst[node] > self._lst[self._parent(node)]:
            self._lst[node], self._lst[self._parent(node)] = self._lst[self._parent(node)], self._lst[node]
            node = self._parent(node)
    
    def heapify_down(self, node: int):
        while self._left(node) < len(self._lst):
            highest = self._lst[node]
            idx_highest = node 
            
            for child in [self._left(node), self._right(node)]:
                if child < len(self._lst):
                    if highest < self._lst[child]:
                        highest = self._lst[child]
                        idx_highest = child 
            
            if idx_highest != node:
                self._lst[node], self._lst[idx_highest] = self._lst[idx_highest], self._lst[node]
                node = idx_highest
            else:
                break
            
    def insert(self, value: int):
        """
        adds a new node to the Binary Tree
        and applies the heapify method to keep the Tree a heap 
        """
        self._lst.append(value)
        self.heapify_up(len(self._lst) - 1)
        
    def pop_max(self) -> int:
        """
        returns the max and removes it from the data structure
        """
        result = self._lst[0]
        self._lst[0] = self._lst[-1]
        self._lst.pop(-1)
        self.heapify_down(0)
        return result 
    
    def __len__(self) -> int:
        return len(self._lst)


def selection_sort(array: list[int]) -> None:
    """
    in-place implemenation of selection sort    
    """
    
    n = len(array)
    for i in range(n): # n iters
        # find the min element in the interval [i, n)
        idx_min = i
        for j in range(i, n): # n - i iters 
            if array[idx_min] > array[j]:
                idx_min = j 
                
        # swap i and the min
        array[i], array[idx_min] = array[idx_min], array[i]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # selection_sort(arr)
    
    h = Heap()
    for element in arr:
        h.insert(element)

    sorted_arr = [None for _ in range(n)]
    while len(h) > 0: # as long as the heap isn't empty
        current_max = h.pop_max() # retrieves the max and removes it at the same time
        sorted_arr[len(h)] = current_max
        
    for x in sorted_arr:
        print(x)
        
        
if __name__ == '__main__':
    main()