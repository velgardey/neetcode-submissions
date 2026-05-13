class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, pick):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True

                    backtrack(perm, pick)

                    pick[i] = False
                    perm.pop()

        backtrack([], [False]*len(nums))
        return res
                    