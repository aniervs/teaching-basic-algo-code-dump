import heapq
from collections import defaultdict

class HuffmanCoder:
    """
    A class to perform Huffman encoding and decoding for any array of immutable objects.
    """
    
    def __init__(self):
        self.codes = {}           # item -> binary code string
        self.reverse_codes = {}   # binary code string -> item
        
    def _build_frequency_table(self, data):
        """
        Builds a frequency table for the immutable objects in the input data array.
        """
        frequency_table = defaultdict(int)
        for item in data:
            frequency_table[item] += 1
        return frequency_table

    def _build_huffman_tree(self, frequency_table):
        """
        Builds a Huffman tree from the frequency table using a min-heap.
        Tree nodes are tuples: (frequency, item_or_None, left_child, right_child)
        """
        if len(frequency_table) == 0:
            return None
        
        if len(frequency_table) == 1:
            # Special case: only one unique item
            item = list(frequency_table.keys())[0]
            freq = frequency_table[item]
            return (freq, item, None, None)
        
        # Create leaf nodes and add to heap
        heap = []
        node_counter = 0  # To ensure stable sorting when frequencies are equal
        
        for item, freq in frequency_table.items():
            # Leaf node: (frequency, counter, item, left=None, right=None)
            heapq.heappush(heap, (freq, node_counter, item, None, None))
            node_counter += 1
        
        # Build tree by merging nodes
        while len(heap) > 1:
            # Get two nodes with lowest frequency
            freq1, _, item1, left1, right1 = heapq.heappop(heap)
            freq2, _, item2, left2, right2 = heapq.heappop(heap)
            
            # Create internal node
            merged_freq = freq1 + freq2
            left_node = (freq1, _, item1, left1, right1)
            right_node = (freq2, _, item2, left2, right2)
            merged_node = (merged_freq, node_counter, None, left_node, right_node)
            
            heapq.heappush(heap, merged_node)
            node_counter += 1
        
        return heap[0]

    def _build_huffman_codes(self, node, current_code=""):
        """
        Recursively builds the Huffman codes dictionary by traversing the tree structure.
        """
        if node is None:
            return
        
        freq, counter, item, left, right = node
        
        # Leaf node - store the code
        if item is not None:
            # Handle special case of single character
            if current_code == "":
                current_code = "0"
            self.codes[item] = current_code
            self.reverse_codes[current_code] = item
            return
        
        # Internal node - recurse on children
        if left is not None:
            self._build_huffman_codes(left, current_code + "0")
        if right is not None:
            self._build_huffman_codes(right, current_code + "1")
    
    def encode(self, data):
        """
        Encodes the input data array.
        Returns a tuple: (encoded_string, huffman_tree)
        """
        if not data:
            return "", None
        
        # Build frequency table
        frequency_table = self._build_frequency_table(data)
        
        # Build Huffman tree
        huffman_tree = self._build_huffman_tree(frequency_table)
        
        # Generate codes
        self.codes = {}
        self.reverse_codes = {}
        self._build_huffman_codes(huffman_tree)
        
        # Encode the data
        encoded_string = ''.join(self.codes[item] for item in data)
        
        return encoded_string, huffman_tree

    def decode(self, encoded_data, huffman_tree):
        """
        Decodes the binary string using the provided Huffman tree.
        Returns the original array of immutable objects.
        """
        if not encoded_data or huffman_tree is None:
            return []
        
        freq, counter, item, left, right = huffman_tree
        
        # Handle single character case
        if item is not None:
            return [item] * len(encoded_data)
        
        decoded_data = []
        current_node = huffman_tree
        
        for bit in encoded_data:
            curr_freq, curr_counter, curr_item, curr_left, curr_right = current_node
            
            # Traverse tree based on bit
            if bit == '0':
                current_node = curr_left
            else:  # bit == '1'
                current_node = curr_right
            
            # Check if we reached a leaf
            if current_node is not None:
                node_freq, node_counter, node_item, node_left, node_right = current_node
                if node_item is not None:
                    decoded_data.append(node_item)
                    current_node = huffman_tree  # Reset to root
        
        return decoded_data

def main_huffman():
    """
    Main function for testing the HuffmanCoder class with a string and a list of tuples.
    """
    print("--- Testing Huffman with a simple string ---")
    text_to_compress = "this is a simple example of huffman encoding"
    
    huffman_coder = HuffmanCoder()
    encoded_text, huffman_tree = huffman_coder.encode(list(text_to_compress))
    decoded_text_list = huffman_coder.decode(encoded_text, huffman_tree)
    decoded_text = "".join(decoded_text_list)
    
    assert text_to_compress == decoded_text, "Decoding failed for string!"
    print(f"Original Text: '{text_to_compress}'")
    print(f"Decoded Text:  '{decoded_text}'")
    print("Huffman Encoding/Decoding works correctly for strings! ✅")

    # Show the generated codes
    print(f"\nHuffman Codes:")
    for char, code in sorted(huffman_coder.codes.items()):
        print(f"  '{char}' -> {code}")

    original_size_bits = len(text_to_compress) * 8
    compressed_size_bits = len(encoded_text)
    compression_rate = (1 - compressed_size_bits / original_size_bits) * 100
    
    print(f"\nOriginal Size (bits): {original_size_bits}")
    print(f"Compressed Size (bits): {compressed_size_bits}")
    print(f"Compression Rate: {compression_rate:.2f}%")

    print("\n" + "="*50 + "\n")

    print("--- Testing Huffman with a list of tuples (simulating LZ77 tokens) ---")
    
    # Example data representing LZ77 tokens
    lz77_tokens = [
        (0, 0, 't'), (0, 0, 'h'), (0, 0, 'i'), (0, 0, 's'), (0, 0, ' '),
        (0, 0, 'i'), (0, 0, 's'), (0, 0, ' '), (0, 0, 'a'), (0, 0, ' '),
        (0, 0, 's'), (0, 0, 'i'), (0, 0, 'm'), (0, 0, 'p'), (0, 0, 'l'),
        (0, 0, 'e'), (0, 0, ' '), (0, 0, 'e'), (0, 0, 'x'), (0, 0, 'a'),
        (0, 0, 'm'), (0, 0, 'p'), (0, 0, 'l'), (0, 0, 'e')
    ]
    
    huffman_coder_tokens = HuffmanCoder()
    encoded_tokens, huffman_tree_tokens = huffman_coder_tokens.encode(lz77_tokens)
    decoded_tokens = huffman_coder_tokens.decode(encoded_tokens, huffman_tree_tokens)
    
    assert lz77_tokens == decoded_tokens, "Decoding failed for tuples!"
    print("Huffman Encoding/Decoding works correctly for a list of tuples! ✅")

    print(f"\nOriginal number of tokens: {len(lz77_tokens)}")
    print(f"Encoded size (bits): {len(encoded_tokens)}")
    
    # More detailed analysis for tuples
    unique_tokens = len(set(lz77_tokens))
    print(f"Unique tokens: {unique_tokens}")
    print(f"Most frequent tokens:")
    freq_table = defaultdict(int)
    for token in lz77_tokens:
        freq_table[token] += 1
    
    for token, freq in sorted(freq_table.items(), key=lambda x: x[1], reverse=True)[:5]:
        code = huffman_coder_tokens.codes.get(token, "N/A")
        print(f"  {token}: {freq} times, code: {code}")

if __name__ == '__main__':
    main_huffman()