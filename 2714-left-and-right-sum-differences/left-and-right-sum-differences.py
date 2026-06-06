class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        tot=sum(nums)
        n=len(nums)
        leftSum=0
        rightSum=tot
        result=[]
        rightSum=rightSum-nums[0]
        result.append(abs(leftSum-rightSum))
        for i in range(1,n):
            leftSum+=nums[i-1]
            rightSum-=nums[i]
            result.append(abs(leftSum-rightSum))
        return result
