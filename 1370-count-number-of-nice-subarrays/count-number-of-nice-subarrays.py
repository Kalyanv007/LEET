class Solution:
    def func(self,arr,goal):
        l=0
        r=0
        n=len(arr)
        sum1=0
        cnt=0
        if goal<0:
            return 0
        while r<n:
            sum1+=(arr[r]%2) #adding 1 or 0
            while sum1>goal:
                sum1=sum1-(arr[l]%2) #subtracting 1 or 0
                l=l+1
            cnt=cnt+(r-l+1) # is calculating for sum<=goal so it takes all subarrays before r into consideration without moving l
            r+=1
        return cnt

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.func(nums,k)-self.func(nums,k-1)