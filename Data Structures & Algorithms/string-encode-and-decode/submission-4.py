class Solution:
    # the point of this code is to covert an array of strings to single string and add a delimiter to seperate strings
    def encode(self, strs: List[str]) -> str: 
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string # i.e. love becomes 4#love
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j 
        return res
