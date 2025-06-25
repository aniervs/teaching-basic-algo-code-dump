class HashTable:
    def __init__(self):
        self.MOD = 2 
        self.BASE = 311 
        self.size = 0
        self.table = ... # TODO: this is a python list of the size of the MOD, that will contain the HEAD of a linked list
    
    def _hash(self, word: str) -> int:
        """
        applies the hash function to the word with the given BASE and MOD
        this is implemented for you
        """
        result = 0
        for i in range(len(word)):
            result = (result * self.BASE + word[i]) % self.MOD 
        return result 
    
    def _table_doubling(self):
        # TODO: double the MOD and recompute the hash of every element 
        raise NotImplementedError()
        
    
    def insert(self, word: str):
        # TODO step 0: if the size gets too big, call the table doubling
        raise NotImplementedError()
        # TODO step 1: compute the hash value of the word (self._hash)
        raise NotImplementedError()
        # TODO step 2: go to self.table and insert the word in the corresponding linked list
        raise NotImplementedError()
    
    def exists(self, word: str):
        # TODO step 1: compute the hash value of the word (self._hash)
        raise NotImplementedError()
        # TODO step 2: go to self.table and check if the word is in the linked list
        raise NotImplementedError()
    
    def remove(self, word: str):
        # TODO step 1: compute the hash value of the word (self._hash)
        raise NotImplementedError()
        # TODO step 2: go to self.table and remove the word from the linked list, if it exists
        raise NotImplementedError()
    
    