class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        l=0
        n=len(nums)
        r=0
        farthest=0
        while(r<n-1):
            
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r+1
            r=farthest
            jumps+=1
        return jumps