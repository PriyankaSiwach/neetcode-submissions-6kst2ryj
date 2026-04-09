class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid), len(grid[0])

        def bfs(r,c):
            if r<0 or c<0 or r>= rows or c>=cols or grid[r][c]=="0":
                return
            else:
                grid[r][c]="0"
                bfs(r-1,c)
                bfs(r+1,c)
                bfs(r,c+1)
                bfs(r,c-1)
        island=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    island+=1
                    bfs(r,c)
                    
        return island
        