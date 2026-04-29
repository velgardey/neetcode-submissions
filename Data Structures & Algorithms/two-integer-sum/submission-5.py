class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, val in enumerate(nums):
            indices[val] = i

        for i, val in enumerate(nums):
            diff = target - val
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
                