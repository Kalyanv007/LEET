class Solution:
    def helper(self,nums,ds,result,freq):
        if len(ds)==len(nums):
            result.append(ds[:])
        for i in range(0,len(nums)):
            if freq[i]==0:
                freq[i]=1
                ds.append(nums[i])
                self.helper(nums,ds,result,freq)
                ds.pop()
                freq[i]=0
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        ds=[]
        freq=[0]*len(nums)
        self.helper(nums,ds,result,freq)
        return result