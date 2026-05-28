class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def checkpalin(l, r):
            nonlocal count

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return

        for i in range( len(s) ):
            # check for odd length palindromes
            l, r = i, i
            checkpalin(l, r)

            #check for even length palindromes
            l, r = i, i + 1
            checkpalin(l, r)

        return count