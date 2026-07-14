class Solution:


    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for _ in range(2)]for _ in range(n+1)]
        dp[n][0]=dp[n][1]=0#last day so buying or selling gives 0 profit
        for i in range(n-1,-1,-1):
            for buy in range(2):
                if not buy:
                    dp[i][buy]=max(dp[i+1][1]-prices[i],0+dp[i+1][0])
                else:
                    dp[i][buy]=max(dp[i+1][1]+0,dp[i+1][0]+prices[i])
        return dp[0][0]
        