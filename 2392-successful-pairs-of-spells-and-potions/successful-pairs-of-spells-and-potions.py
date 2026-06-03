class Solution:
    def binarySearch(self,num,arr,k):
        n=len(arr)
        low=0
        high=n-1
        ans=n
        while(low<=high):
            mid=(low+high)//2
            if (num*arr[mid]>=k):
                ans=mid
                high=mid-1
            elif(num*arr[mid]<k):
                low=mid+1
        return n-ans

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs=[]
        potions.sort()
        for i in range(len(spells)):
            pairs.append(self.binarySearch(spells[i],potions,success))
        return pairs
