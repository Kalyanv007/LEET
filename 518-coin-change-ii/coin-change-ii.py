class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0 for _ in range(amount+1)]for _ in range(n)]
        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[0][target] = 1
            else:
                dp[0][target] = 0
        
        for i in range(1,n):
            for target in range(amount+1):
                notTake=dp[i-1][target]
                take=0
                if coins[i]<=target:
                    take=dp[i][target-coins[i]]
                dp[i][target]=take+notTake
        return dp[n-1][amount]