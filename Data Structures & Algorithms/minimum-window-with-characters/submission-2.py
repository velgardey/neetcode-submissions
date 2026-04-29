class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge Case to handle empty string t 
        if t == "":
            return ""

        # Initiate hashmaps for 1. keeping freq of chars in the string t, and 2. keeping freq of chars in the current window
        freq, window = {}, {}

        # Populate the freq hashmap
        for c in t:
            freq[c] = 1 + freq.get(c, 0)

        # initiate a need and a have variable to store the requirement count and the target requirement count
        have, need = 0, len(freq)

        # initiate a res pair [l, r] to store the window pointers and resLength to store the least window size
        res, resLength = [-1, -1], float("infinity")
        
        # initiate the sliding window to check 
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0) # increment freq count in window hashmap

            if s[r] in freq and window[s[r]] == freq[s[r]] :
                have += 1   # if one of the required chars has fulfilled necessary freq, update have by 1
            
            # Now check if we have satisfied the need req
            while have == need :
                if ( r- l + 1 ) < resLength : # If the current window size is smaller than the current smallest window size
                    res = [l, r]
                    resLength = r - l + 1
                    
                # then we decrease the window to check if we can reduce the required window length
                window[s[l]] -= 1  # decrease window size by removing the char from the freq map

                if s[l] in freq and window[s[l]] < freq[s[l]]:
                    have -= 1     # check if upon reducing window size, we have removed a char necessary for meeting one of the requirements

                l += 1  # decrease window size by pointer 
        
        l, r = res
        return s[l : r + 1] if resLength != float("infinity") else ""


