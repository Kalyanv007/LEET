class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        output = 0
        g.sort()
        s.sort()
        i=0
        j=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                output+=1
                i+=1
                j+=1
            else:
                j+=1

        return output


