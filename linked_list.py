class Node:
    def __init__(self, data: int):
        self.data = data 
        self.next = None # initially a node points to NULL

class LinkedList:
    def __init__(self):
        self.head = None # it's an empty LinkedList 
        self.tail = None # it's an empty LinkedList
        
    def append_right(self, new_data: int):
        new_node = Node(new_data)
        if self.head is None: # edge case where the linked list is empty 
            self.head = new_node 
            self.tail = new_node 
        else:
            # linked list is not empty (both head and tail are not None)
            self.tail.next = new_node 
            self.tail = new_node 
            
    def append_left(self, new_data: int):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node 
        
    def pop_right(self):
        assert self.head is not None, 'LIST is empty!!!'

        if self.head == self.tail:
            # that means that the list contains a single element
            self.head = None 
            self.tail = None 
        else:
            current_node = self.head 
            while current_node.next != self.tail:
                current_node = current_node.next 
            self.tail = current_node
         
    def pop_left(self):
        assert self.head is not None, 'LIST is empty!!!'
        # the list is not empty 
        self.head = self.head.next 
        # edge case:
        if self.head is None:
            self.tail = None 
           
    def __getitem__(self, k: int):
        """
        A function that returns the k-th element 
        """
        current_node = self.head 
        for _ in range(k):
            current_node = current_node.next
        return current_node.data

    def __setitem__(self, k: int, new_value: int):
        """
        updates the value of the k-th element to new_value
        """
        current_node = self.head 
        for _ in range(k):
            current_node = current_node.next
        current_node.data = new_value
    
    def __delitem__(self, k: int):
        """removes the k-th item"""
        raise Exception("TO IMPLEMENT")
        pass 
    

l = LinkedList()
l.append_right(3)
l.append_right(4)
l.append_right(7)
l.append_right(11)
print(l[2])
    
    