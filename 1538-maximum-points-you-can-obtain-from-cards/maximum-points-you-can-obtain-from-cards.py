class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        lSum=0
        maxSum=0
        for i in range(k):
            lSum+=cardPoints[i]
        maxSum=lSum
        rindex=n-1
        rSum=0
        for i in range(k-1,-1,-1):
            lSum=lSum-cardPoints[i]
            rSum+=cardPoints[rindex]
            maxSum=max(maxSum,lSum+rSum)
            rindex-=1
        return maxSum