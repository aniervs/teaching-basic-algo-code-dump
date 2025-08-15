import time
import random
import string
from tqdm import tqdm 

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
    
class LinkedList:
    def __init__(self):
        self.head = None 
    
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head 
            while current_node.next is not None:
                current_node = current_node.next 
            current_node.next = node 
    def remove(self, data):
        assert self.head is not None 
        previous = None 
        current_node = self.head 
        while current_node is not None and current_node.data != data:
            previous = current_node
            current_node = current_node.next 
        
        assert current_node is not None
        if previous is not None:
            previous.next = current_node.next 
            del current_node
        else:
            self.head = current_node.next 
            
    def exists(self, data):
        current_node = self.head 
        while current_node is not None and current_node.data != data:
            current_node = current_node.next 
        if current_node is not None:
            return True 
        return False 
    
    def clear(self):
        self.head = None
        
    def __iter__(self):
        current_node = self.head 
        while current_node is not None:
            yield current_node.data 
            current_node = current_node.next 

class HashTable:
    def __init__(self):
        self.MOD = 2
        self.BASE = 311 
        self.size = 0
        self.table = [LinkedList() for _ in range(self.MOD)]
    
    def _hash(self, word: str) -> int:
        result = 0
        for i in range(len(word)):
            result = (result * self.BASE + ord(word[i])) % self.MOD 
        return result 
    
    def _table_doubling(self):
        tmp_list = []
        for m in range(0, self.MOD):
            for value in self.table[m]:
                tmp_list.append(value)
            self.table[m].clear()
        
        self.MOD *= 2 
        self.table = [LinkedList() for _ in range(self.MOD)]
        for value in tmp_list:
            hash_value = self._hash(value)
            self.table[hash_value].append(value)
           
    def insert(self, word: str):
        if self.exists(word):
            return 
        self.size += 1
        if 2 * self.size > self.MOD:
            self._table_doubling()
        hash_value = self._hash(word)
        self.table[hash_value].append(word)
    
    def exists(self, word: str):
        hash_value = self._hash(word)
        return self.table[hash_value].exists(word)
    
    def remove(self, word: str):
        hash_value = self._hash(word)
        if self.table[hash_value].exists(word):
            self.table[hash_value].remove(word)
            self.size -= 1  

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def stress_test_hash_table(n=1000_000):
    ht = HashTable()
    words = [generate_random_string() for _ in range(n)]

    print(f"Inserting {n} elements...")
    t1 = time.time()
    for word in tqdm(words):
        ht.insert(word)
    t2 = time.time()
    print(f"Time to insert: {t2 - t1:.4f} seconds")
    
    print("Checking existence of all inserted elements...")
    t3 = time.time()
    assert all(ht.exists(word) for word in tqdm(words))
    t4 = time.time()
    print(f"Time to check existence: {t4 - t3:.4f} seconds")

    print("Removing half of the elements...")
    t5 = time.time()
    for word in tqdm(words[:n // 2]):
        ht.remove(word)
    t6 = time.time()
    print(f"Time to remove: {t6 - t5:.4f} seconds")

    print("Validating correctness after removal...")
    for word in tqdm(words[:n // 2]):
        assert not ht.exists(word)
    for word in tqdm(words[n // 2:]):
        assert ht.exists(word)
    print("Correctness check passed.")

    total_ops = 2 * n 
    total_time = (t2 - t1) + (t4 - t3) + (t6 - t5)
    avg_time = total_time / total_ops
    print(f"\nAverage time per operation: {avg_time:.10f} seconds")

    if avg_time < 1e-5:
        print("✅ HashTable performs in average-case O(1) time.")
    else:
        print("⚠️ HashTable may have performance issues to investigate.")

stress_test_hash_table(100_000)