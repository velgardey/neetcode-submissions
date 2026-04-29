class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we put unreachable values in each dp array position to check for invalid dp amounts
        dp = [amount + 1] * (amount + 1)  # i.e. dp[0] to dp[amount]
        # we put dp[0] as 0 as no coins can be combined to make up the amount 0
        dp[0] = 0

        for amount_value in range(1, amount + 1): # i.e. from 1 to amount
            for coin_value in coins:
                if amount_value - coin_value >= 0:
                    dp[amount_value] = min(dp[amount_value], 1 + dp[amount_value - coin_value]) # we are checking if the present memoized value can be lessened by using another coin_value instead as it is iterating over all the cain_values
        return dp[amount] if dp[amount] != (amount + 1) else -1 
