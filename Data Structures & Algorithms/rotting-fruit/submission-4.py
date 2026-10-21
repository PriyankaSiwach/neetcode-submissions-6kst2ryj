class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid), len(grid[0])
        visit=set()
        q=deque()
        directions= [(1,0), (-1,0), (0,1), (0,-1)]
        time,fresh=0,0
        def bfs(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1:
                return 
            grid[r][c]=2
            fresh-=1
            q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        while q and fresh>0:
            for i in range(len(q)):
                r,c= q.popleft()
                for dr,dc in directions:
                    nr,nc= dr+r,dc+c
                    bfs(nr,nc)
            time+=1
        return time if fresh==0 else -1

                    

