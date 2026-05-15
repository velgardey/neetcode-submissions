class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buyState):

            if i >= len(prices):
                return 0
            
            if (i, buyState) in dp:
                return dp[(i, buyState)]
            
            if buyState == True:
                buy = dfs(i + 1, not buyState) - prices[i]
                cooldown = dfs(i + 1, buyState)
                dp[(i, buyState)] = max( buy, cooldown)
            else:
                sell = dfs(i + 2, not buyState) + prices[i]
                cooldown = dfs(i+1, buyState)
                dp[(i, buyState)] = max( sell, cooldown )
            
            return dp[(i, buyState)]

        return dfs(0, True)