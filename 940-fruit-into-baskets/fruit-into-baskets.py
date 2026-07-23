class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        freq={}
        maxcount=0
        k=2
        for right in range(len(fruits)):
            freq[fruits[right]]=freq.get(fruits[right],0)+1
            while len(freq)>k:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            maxcount=max(maxcount,right-left+1)
        return maxcount
    


