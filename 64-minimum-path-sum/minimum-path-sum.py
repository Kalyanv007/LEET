class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for _ in range(m)]for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                    continue
                up=grid[i][j]
                left=grid[i][j]
                if i>0:
                    up+=dp[i-1][j]
                else:
                    up+=1e9
                if j>0:
                    left+=dp[i][j-1]
                else:
                    left+=1e9
                dp[i][j]=min(up,left)
        return dp[n-1][m-1]
