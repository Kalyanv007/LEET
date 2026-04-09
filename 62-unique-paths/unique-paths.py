class Solution:
    def calc(self,m,n,dp):
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                left=0
                up=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        
        return dp[m-1][n-1]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)]for i in range(m)]
        return self.calc(m,n,dp)