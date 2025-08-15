class Node:
    def __init__(self):
        self.children = dict() # letter -> node 
        self.is_word = False 

class Trie:
    def __init__(self):
        self.root = Node()
        
    def add_word(self, word: str):
        current_node = self.root 
        for char in word:
            if char not in current_node.children: # if the link doesn't exist
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.is_word = True # this node corresponds to a full word in the data structure
    
    def check_word(self, word: str) -> bool: 
        current_node = self.root 
        for char in word:
            if char not in current_node.children: # if the link doesn't exist
                return False 
            current_node = current_node.children[char]
        return current_node.is_word
    
    def remove_word(self, word: str) -> bool:
        # TODO in homework
        raise NotImplementedError()

