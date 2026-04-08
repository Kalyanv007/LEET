class Solution:
    def solve(self,nums):
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        neg=0
        for i in range(1,n):
            take=nums[i]
            if(i>1):
                take+=dp[i-2]
            notTake=0+dp[i-1]
            dp[i]=max(take,notTake)
        return dp[n-1]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
         # arr1 excludes first house
        arr1 = nums[1:]
        # arr2 excludes last house
        arr2 = nums[:-1]
        return(max(self.solve(arr1),self.solve(arr2)))
        
        