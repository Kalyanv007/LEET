class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.combination(candidates,target,[],0)
        return self.res
        
    def combination(self,candidates,target,temp,index):
        if target==0:
            self.res.append(temp[:])
            return
        for i in range(index,len(candidates)):
            if candidates[i]<=target:
                temp.append(candidates[i])
                self.combination(candidates,target-candidates[i],temp,i)
                temp.pop()
        
