class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col=[]
        n=len(grid)
        count=0
        for i in range(n):
            cols=[]
            for j in range(n):
                cols.append(grid[j][i])
            col.append(cols)
        
        for c in col:
            for r in grid:
                if c == r:
                    count += 1
        return count
        