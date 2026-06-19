class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur=0
        maxi=0
        for g in gain:
            cur+=g
            maxi=max(maxi,cur)
        return maxi