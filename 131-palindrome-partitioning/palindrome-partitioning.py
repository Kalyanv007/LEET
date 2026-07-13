class Solution:
    def is_palindrome(self,str1):
        return str1==str1[::-1]
    
    def helper(self, ind, s, ds, result):
        if ind == len(s):
            result.append(ds[:])
            return

        for i in range(ind, len(s)):
            substring = s[ind:i+1]

            if self.is_palindrome(substring):
                ds.append(substring)
                self.helper(i + 1, s, ds, result)
                ds.pop()
    def partition(self, s: str) -> List[List[str]]:
        result = []
        ds = []
        self.helper(0, s, ds, result)
        return result