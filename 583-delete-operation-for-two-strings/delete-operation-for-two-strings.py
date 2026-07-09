class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=0
        for j in range(m+1):
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=0+max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
    def minDistance(self, word1: str, word2: str) -> int:
        return len(word1)+len(word2)-(2*self.longestCommonSubsequence(word1,word2)) # deletions=n-lcs and insertions=m-lcs so total ops is the sum