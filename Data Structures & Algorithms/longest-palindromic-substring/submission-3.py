class Solution:
    def longestPalindrome(self, s: str) -> str:
        # two pointers method
        resIdx = 0 # starting index of the result sub string
        resLength = 0 # length of the result sub string

        for i in range(len(s)):
            # for odd length of palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ( r - l + 1 ) > resLength:
                    resIdx = l
                    resLength = r - l + 1
                l -= 1
                r += 1

            # for even length of palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if ( r - l + 1 ) > resLength:
                    resIdx = l
                    resLength = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLength]