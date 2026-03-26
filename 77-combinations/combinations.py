class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        temp=[]
        num=1
        def combinations(temp,num):
            #goal state
            if (len(temp)==k):
                res.append(temp[:])
                return
            #exploration 
            for i in range(num,n+1):
                temp.append(i) #action
                combinations(temp,i+1)#recursive call
                temp.pop()#backtracking

        combinations(temp,num)
        return res

            