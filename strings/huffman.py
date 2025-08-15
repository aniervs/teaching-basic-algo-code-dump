import heapq
from collections import defaultdict

class HuffmanCoder:
    """
    A class to perform Huffman encoding and decoding for any array of immutable objects.
    """
    
    def __init__(self):
        pass 
        
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
        """
        pass 
        raise NotImplementedError()
        

    def _build_huffman_codes(self, node, current_code=""):
        """
        Recursively builds the Huffman codes dictionary by traversing the corrected tree structure.
        """
        pass 
        raise NotImplementedError()    
    
    def encode(self, data):
        """
        Encodes the input data array.
        Returns a tuple: (encoded_string, huffman_tree)
        """
        pass 
        raise NotImplementedError()

    def decode(self, encoded_data, huffman_tree):
        """
        Decodes the binary string using the provided Huffman tree.
        Returns the original array of immutable objects.
        """
        pass 
        raise NotImplementedError()
    
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
    print("Note: The compression rate here is an approximation, as the original size "
          "in bits depends on the bit representation of each token (offset, length, char).")

if __name__ == '__main__':
    main_huffman()
    