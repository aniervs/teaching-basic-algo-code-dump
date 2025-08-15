class LZ77Coder:
    """
    A class to perform LZ77 encoding and decoding.
    """
    def __init__(self, window_size, lookahead_buffer_size):
        self.window_size = window_size
        self.lookahead_buffer_size = lookahead_buffer_size

    def encode(self, data):
        """
        Encodes the input data using the LZ77 algorithm.
        Returns a list of (offset, length, next_char) tuples.
        """
        tokens = []
        i = 0
        
        while i < len(data):
            # Define search and lookahead buffers
            start = max(0, i - self.window_size)
            search_buffer = data[start:i]
            end = min(i + self.lookahead_buffer_size, len(data))
            lookahead_buffer = data[i:end]
            
            if not lookahead_buffer:  # End of data
                break
                
            best_offset, best_len = 0, 0
            
            # Search for longest match in search buffer
            for j in range(len(search_buffer)):
                match_length = 0
                
                # Compare characters starting from position j in search buffer
                while (j + match_length < len(search_buffer) and 
                       match_length < len(lookahead_buffer) and 
                       search_buffer[j + match_length] == lookahead_buffer[match_length]):
                    match_length += 1
                
                # Update best match if this one is longer
                if match_length > best_len:
                    best_offset = len(search_buffer) - j
                    best_len = match_length
            
            # Create token with next character
            if best_len > 0:
                next_char_pos = best_len
                next_char = lookahead_buffer[next_char_pos] if next_char_pos < len(lookahead_buffer) else ''
                tokens.append((best_offset, best_len, next_char))
                i += best_len + (1 if next_char else 0)
            else:
                # No match found, output literal character
                tokens.append((0, 0, lookahead_buffer[0]))
                i += 1
        
        return tokens

    def decode(self, encoded_data):
        """
        Decodes the LZ77 encoded data.
        Returns the original string.
        """
        decoded = []
        
        for offset, length, next_char in encoded_data:
            if length > 0:
                # We have a match - copy from previous data
                start_pos = len(decoded) - offset
                
                if start_pos < 0:
                    # Invalid offset - shouldn't happen with correct encoding
                    print(f"Warning: Invalid offset {offset} at position {len(decoded)}")
                    continue
                
                # Copy 'length' characters starting from start_pos
                for i in range(length):
                    copy_pos = start_pos + i
                    if copy_pos < len(decoded):
                        decoded.append(decoded[copy_pos])
                    else:
                        # This might happen with overlapping patterns
                        # Use modulo to wrap around the matched pattern
                        pattern_length = min(offset, length)
                        wrapped_pos = start_pos + (i % pattern_length)
                        if wrapped_pos < len(decoded):
                            decoded.append(decoded[wrapped_pos])
            
            # Add the next character (if any)
            if next_char:
                decoded.append(next_char)
        
        return ''.join(decoded)

def main_lz77():
    """Main function for testing the LZ77Coder class."""
    text_to_compress = "aabacaadaaaba"
    window_size = 10
    lookahead_buffer_size = 5
    
    lz77_coder = LZ77Coder(window_size, lookahead_buffer_size)
    
    # Encoding and Decoding
    encoded_tokens = lz77_coder.encode(text_to_compress)
    decoded_text = lz77_coder.decode(encoded_tokens)

    print(f"Original: '{text_to_compress}'")
    print(f"Tokens: {encoded_tokens}")
    print(f"Decoded: '{decoded_text}'")

    # Verification
    assert text_to_compress == decoded_text, "Decoding failed!"
    print("LZ77 Encoding/Decoding works correctly! ✅")

if __name__ == '__main__':
    main_lz77()