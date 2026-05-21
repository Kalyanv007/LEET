class Solution:
    def targetSum(self, arr, target):
        n = len(arr)

        dp = [[False for _ in range(target + 1)] for _ in range(n)]

        # Sum 0 is always possible
        for i in range(n):
            dp[i][0] = True

        # First element
        if arr[0] <= target:
            dp[0][arr[0]] = True

        # Fill DP table
        for i in range(1, n):
            for j in range(target,0,-1):

                notTaken = dp[i-1][j]

                taken = False
                if arr[i] <= j:
                    taken = dp[i-1][j-arr[i]]

                dp[i][j] = taken or notTaken

        return dp[n-1][target]
    def canPartition(self, nums: List[int]) -> bool:
        sum0=sum(nums)
        if sum0%2==1:
            return False
        else:
            return self.targetSum(nums,sum0//2)