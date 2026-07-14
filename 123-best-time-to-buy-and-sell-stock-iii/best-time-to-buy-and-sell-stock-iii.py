class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0 for _  in range(3)]for _ in range(2)]for _ in range(n+1)] #3 for cap(limists) and 2 for buy or sell 
        for i in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if not buy:
                        dp[i][buy][cap]=max(-prices[i]+dp[i+1][1][cap],0+dp[i+1][0][cap])
                    else:
                        dp[i][buy][cap]=max(0+dp[i+1][1][cap],prices[i]+dp[i+1][0][cap-1])
        return dp[0][0][2]