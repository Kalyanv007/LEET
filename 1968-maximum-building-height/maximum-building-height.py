class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if len(restrictions)==0:
            return n-1
        restrictions.append([1,0])
        restrictions.sort(key=lambda x:x[0])
        maxHeight=0
        for i in range(1, len(restrictions)):
            dist = restrictions[i][0] - restrictions[i-1][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i-1][1] + dist
            )
        for i in range(len(restrictions)-2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i+1][1] + dist
            )
        for i in range(len(restrictions)-1):
            maxHeight=max((restrictions[i][1]+restrictions[i+1][1]+restrictions[i+1][0]-restrictions[i][0])//2,maxHeight)

        maxHeight = max(
            maxHeight,
            restrictions[-1][1] + (n - restrictions[-1][0]) #for the last building which matters only on the last restriction and will not be in the middle of up and down 
        )
        return maxHeight
