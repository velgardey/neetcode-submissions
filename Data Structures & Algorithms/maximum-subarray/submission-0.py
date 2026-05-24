class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArr = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSubArr = max(maxSubArr, curSum)
        
        return maxSubArr