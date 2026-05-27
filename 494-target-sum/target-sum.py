class Solution:
    def countSubsets(self, arr, K):
        # Get number of elements
        n = len(arr)

        # Create dp table with dimensions n x (K+1)
        dp = [[0] * (K + 1) for _ in range(n)]

         # Special base case for zero
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        # If first element is non-zero and within range
        if arr[0] != 0 and arr[0] <= K:
            dp[0][arr[0]] = 1

        # Fill the table
        for i in range(1, n):
            for target in range(K + 1):
                # Exclude current element
                notTake = dp[i - 1][target]

                # Include current element if possible
                take = 0
                if arr[i] <= target:
                    take = dp[i - 1][target - arr[i]]

                # Total ways
                dp[i][target] = notTake + take

        # Final answer
        return dp[n - 1][K]
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        totSum=sum(nums)
        if totSum<target or (totSum-target)%2!=0:
            return 0
        return self.countSubsets(nums,(totSum-target)//2)
    