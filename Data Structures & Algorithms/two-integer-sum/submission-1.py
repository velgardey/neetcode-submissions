class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we create a hashmap to map the value on the array to the index
        index = {}

        # now we populate the map
        for i, n in enumerate(nums): # enumerate gives (index, value)
            index[n] = i  

        for i, n in enumerate(nums):
            diff = target - n
            if diff in index and index[diff] != i:
                return [i, index[diff]]