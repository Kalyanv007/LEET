class Solution:
    def rob(self, nums: List[int]) -> int:
        # n=len(nums)
        # dp=[0]*n
        # dp[0]=nums[0]
        # neg=0
        # for i in range(1,n):
        #     take=nums[i]
        #     if(i>1):
        #         take+=dp[i-2]
        #     notTake=0+dp[i-1]
        #     dp[i]=max(take,notTake)
        # return dp[n-1]

        n=len(nums)
        prev=nums[0]
        prev2=0
        for i in range(1,n):
            take=nums[i]
            if(i>1):
                take+=prev2
            notTake=0+prev
            curi=max(take,notTake)
            prev2=prev
            prev=curi
        return prev