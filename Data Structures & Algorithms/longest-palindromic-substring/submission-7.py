class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        def checkpalin(l, r):
            nonlocal res, reslen
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (r - l + 1) > reslen:
                    res = s[l:r + 1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            return

        for i in range(len(s)):

            # checking for odd length palindromes
            checkpalin(i, i)

            #checking for even length palindromes
            checkpalin(i, i + 1)

        return res