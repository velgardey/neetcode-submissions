class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # for odd length of substring
            l, r = i, i # both in the middle character
            while l >= 0 and r < len(s) and s[l] == s[r]: # check bounds and verify palindromity
                res += 1
                l -= 1 # expand to the left
                r += 1 # expand to the right
            
            # for even length of substring
            l, r = i, i + 1 # in case of even lengths, we take two middle chars which are the same
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res