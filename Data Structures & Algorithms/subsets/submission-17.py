class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        set = []

        def dfs(i):
            if i == len(nums):
                res.append(set.copy())
                return
            
            # Choose
            set.append(nums[i])
            dfs(i + 1)
            # Not choose
            set.pop()
            dfs(i + 1)

        dfs(0)
        return res