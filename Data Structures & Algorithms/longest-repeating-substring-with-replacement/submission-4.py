class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = {} # Set up a hashmap to store the freq of the letters
        result = 0

        # Sliding Window Part
        l = 0
        maxFreq = 0
        for r in range(len(s)) :
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxFreq = max(maxFreq, freqMap[s[r]])

            while (r - l + 1) - maxFreq > k :
                freqMap[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        return result