class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {} # Set up a hashmap to store the freq of the letters
        result = 0  # Initialize result int

        # Sliding Window Part
        l = 0 # Both l and r set to 0 intially
        maxFreq = 0 # Set up a variable to store the max freq as it is the only info needed from the hashmap, so we skip the 26 * n time complexity
        for r in range(len(s)) :
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0) # Increment freq of element at r index
            maxFreq = max(maxFreq, freqMap[s[r]]) # Update the max freq with the incremented element

            while (r - l + 1) - maxFreq > k : # Check if the window_size - max_freq <= k has been violated 
                freqMap[s[l]] -= 1 
                l += 1  # Shift the l pointer to the next char and decrement the frequency of the element left by l

            result = max(result, r - l + 1) # Update the result with the valid window size every loop
        return result