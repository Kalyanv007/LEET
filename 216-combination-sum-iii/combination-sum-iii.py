class Solution:
    def helper(self,ind,k,n,ds,result):
        if n==0 and len(ds)==k:
            result.append(ds[:])
            return
        for i in range(ind,10):
            if i>n:
                break
            ds.append(i)
            self.helper(i+1,k,n-i,ds,result)
            ds.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        ds=[]
        self.helper(1,k,n,ds,result)
        return result