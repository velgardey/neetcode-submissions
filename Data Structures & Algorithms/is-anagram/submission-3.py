class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first we check if the strings are the same length or not
        if len(s) != len(t):
            return False
        
        # we make two seperate hashmaps to store the char frequencies
        countS, countT =  {}, {}

        # we populate the hashmaps 
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
        