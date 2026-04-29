class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums: List[int]) -> int:
        robMinusTwo, robMinusOne = 0, 0
        for num in nums:
            temp = max( num + robMinusTwo, robMinusOne)
            robMinusTwo = robMinusOne
            robMinusOne = temp
        return robMinusOne