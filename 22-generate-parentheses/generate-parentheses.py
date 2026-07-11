class Solution:
    def helper(self,openCount,closedCount,ds,result,n):
        if len(ds)==2*n:
            result.append(ds)
            return
        if openCount<n:
            ds+="("
            self.helper(openCount+1,closedCount,ds,result,n)
            ds=ds[:-1]
        if closedCount<openCount:
            ds+=")"
            self.helper(openCount,closedCount+1,ds,result,n)
            ds=ds[:-1]
           
    def generateParenthesis(self, n: int) -> List[str]:
        ds=""
        result=[]
        self.helper(0,0,ds,result,n)
        return result