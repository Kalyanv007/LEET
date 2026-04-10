class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for _ in range(n)]for i in range(m)]
        dp[0][0]=1
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                left=0
                up=0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        
        return dp[m-1][n-1]