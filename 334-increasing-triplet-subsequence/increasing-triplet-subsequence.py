class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=float('inf')
        second=float('inf')
        for num in nums:
            if num<=first:
                first=num
            elif num<=second: #in the first itself if num is smaller than first the only first gets updated cause the smallest number will be a part of the sequence anyway and if the first gets updated mid way that means that there WAS a smaller number anyway and if there exists a greater number then a sequence will be found so it doenst matter if the first gets updated
                second=num
            else:
                return True
        return False