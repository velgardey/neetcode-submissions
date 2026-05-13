class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count == 1:
                if c == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // c
        
        return res