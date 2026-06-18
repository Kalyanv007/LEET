class Solution:
    # def atMost(self, nums, k):

    #     left = 0
    #     right = 0

    #     freq = {}
    #     count = 0

    #     while right < len(nums):

    #         freq[nums[right]] = freq.get(nums[right], 0) + 1

    #         while len(freq) > k:

    #             freq[nums[left]] -= 1

    #             if freq[nums[left]] == 0:
    #                 del freq[nums[left]]

    #             left += 1

    #         count += (right - left + 1)

    #         right += 1

    #     return count
    def numberOfSubstrings(self, s: str) -> int:
        #return self.atMost(s,3)-self.atMost(s,2)
        count=0
        lastSeen=[-1,-1,-1]
        for i in range(len(s)):
            lastSeen[ord(s[i]) - ord('a')]=i
            if -1 not in lastSeen:
                count+=(1+min(lastSeen))
        return count