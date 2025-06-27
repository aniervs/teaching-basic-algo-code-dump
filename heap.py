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
        """
        as long as the parent has less priority than itself,
        it swaps it with its parent's
        """
        while node != 0 and self._lst[node] > self._lst[self._parent(node)]:
            self._lst[node], self._lst[self._parent(node)] = self._lst[self._parent(node)], self._lst[node]
            node = self._parent(node)
    
    def heapify_down(self, node: int):
        while self._left(node) < len(self._lst):
            highest = self._lst[node]
            idx_highest = node 
            
            for child in [self._left(node), self._right(node)]:
                if child < len(self._lst): # if the child exists
                    if highest < self._lst[child]:
                        highest = self._lst[child]
                        idx_highest = child 
            
            if idx_highest != node:
                self._lst[node], self._lst[idx_highest] = self._lst[idx_highest], self._lst[node]
                node = idx_highest
            else:
                break

    def pop_max(self) -> int:
        """
        returns the max and removes it from the data structure
        """
        result = self._lst[0]
        self._lst[0] = self._lst[-1]
        self._lst.pop(-1)
        self.heapify_down(0)
        return result 
    
    def __len__(self):
        return len(self._lst)
        
class PriorityQueue:
    def __init__(self):
        self.heap = Heap()
    def schedule(self, job: int):
        self.heap.insert(job)
    def process_highest_priority_job(self):
        job = self.heap.pop_max()
        return job 
        
def heap_sort(lst: list) -> list:
    """
    returns a sorted copy of the original list
    time complexity: O(n log n)
    """
    h = Heap()
    for x in lst:
        h.insert(x)
    result_lst = [None for _ in range(len(lst))]  
    while len(h) > 0: # O(n) iterations
        max_element = h.pop_max() # O(log n)
        result_lst[len(h)] = max_element
    return result_lst 

def main():
    
    arr = [2, 1, 7, 15, 14, 0, 21, 8, 100, 5, -7, -1, 0, 77, 1000]
    sorted_arr = heap_sort(arr)
    
    print(arr)
    print(sorted_arr)
    
    
    # T = Heap()
    # for x in [2, 1, 7, 15, 14, 0, 21, 8, 100, 5, -7, -1, 0, 77, 1000]:
    #     T.insert(x)
    
    # while len(T) > 0:
    #     max_element = T.pop_max()
    #     print(max_element, end = ' ')
    # print()
    

if __name__ == '__main__':
    main()
