class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Creating dp array of size amount+1
        dp = [float('inf')] * (amount + 1)

        # Base case: dp[0] = 0
        dp[0] = 0

        # Loop through all amounts from 1 to amount
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                # If coin can be used
                if i - coin >= 0 and dp[i - coin] != float('inf'):
                    # Update dp[i] with minimum coins
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # If dp[amount] is still infinity, return -1
        return -1 if dp[amount] == float('inf') else dp[amount]