class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):

            for prev_ind in range(ind - 1, -2, -1):

                notTake = dp[ind + 1][prev_ind + 1]

                take = 0
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    take = 1 + dp[ind + 1][ind + 1]

                dp[ind][prev_ind + 1] = max(take, notTake)

        return dp[0][0]