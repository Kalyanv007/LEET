class Solution:
    def longestPrefix(self, s: str) -> str:
        n=len(s)
        prefix_function=[0]*n
        j=0
        for i in range(1,n):
            while j>0 and s[i]!=s[j]:
                j=prefix_function[j-1]
            if s[i]==s[j]:
                j+=1
            prefix_function[i]=j
        length=prefix_function[-1]
        return s[:length]