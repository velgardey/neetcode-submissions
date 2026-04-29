class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers method
        resIdx, resLength = 0, 0

        for i in range(len(s)):
            # for odd lengths
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ( r - l + 1 ) > resLength:
                    resIdx = l
                    resLength = r - l + 1
                l -= 1
                r += 1

            # for even lengths
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ( r - l + 1 ) > resLength:
                    resIdx = l
                    resLength = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLength]