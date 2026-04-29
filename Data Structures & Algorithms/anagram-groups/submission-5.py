class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # it creates a default value (in this case it is a list) 
        # the above map keeps track of the 

        for string in strs:
            count = [0] * 26 # count is the array which stores the freq of the chars
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)
        return list(res.values())