class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        row=[0]*cols
        row[cols-1]=grid[rows-1][cols-1]
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if r==rows-1 and c==cols-1:
                    continue
                if r== rows-1:
                    row[c]=grid[r][c]+ row[c+1]
                if c==cols-1:
                    row[c]= grid[r][c]+ row[c]
                else:
                    row[c]= grid[r][c]+ min(row[c],row[c+1])
        return row[0]
