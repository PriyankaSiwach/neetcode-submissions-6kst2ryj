class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows,cols= len(grid), len(grid[0])
        rowcount=[0]*rows
        colcount=[0]*cols
        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    rowcount[r]+=1
                    colcount[c]+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if rowcount[r]>1 or colcount[c]>1:
                        res+=1
        return res

                    