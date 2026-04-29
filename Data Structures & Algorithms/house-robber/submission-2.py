class Solution:
    def rob(self, nums: List[int]) -> int:
        robMinusTwo = 0 # rob1 stores the maxm possible loot from the prev to prev house i.e. two houses back
        robMinusOne = 0 # rob2 stores the maxm possible loot from the prev house i.e. one house back

        for num in nums:
            temp = max(num + robMinusTwo, robMinusOne)  # we check if the rob1 and the current loot is the better choice or the rob2 house outweighs the maxm
            robMinusTwo = robMinusOne # shifting the current one house back to two houses back
            robMinusOne = temp # shifting the current one back to one house back
        
        return robMinusOne  # since we are max comparing the current maxm and storing it in robMinusOne
        