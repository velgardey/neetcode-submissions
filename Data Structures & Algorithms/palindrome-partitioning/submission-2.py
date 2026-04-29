class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, cur_part = [], []

        def isPalindrome(string, l, r):
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(i): # i is the index of the starting char in the string
            if i >= len(s): # we check if the current index is at the end of the string
                res.append(cur_part.copy()) # we append the current parititon array along this branch combination in the backtracking decision tree
                return
            for j in range(i, len(s)): # we check from ith index till the end of the string
                if isPalindrome(s, i, j):
                    cur_part.append(s[i:j + 1])
                    dfs(j + 1) # we call dfs from the next char in the string
                    cur_part.pop() # as we have already added the partiton to res in the base case, we have to clean it up for other branches and possible partitions


        dfs(0) # start from the starting index of the string
        return res

