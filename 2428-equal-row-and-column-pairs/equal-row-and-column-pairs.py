class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        rows = {}

        # Store row frequencies
        for row in grid:
            t = tuple(row)
            rows[t] = rows.get(t, 0) + 1

        count = 0

       
        for j in range(n):
            col = []

            for i in range(n):
                col.append(grid[i][j])

            count += rows.get(tuple(col), 0)

        return count