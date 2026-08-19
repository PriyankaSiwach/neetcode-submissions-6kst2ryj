class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid), len(grid[0])
        visit=set()
        time=0
        q=deque()
        fresh=0
        def bfs(r,c):
            nonlocal fresh
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1:
                return 0
            grid[r][c]=2
            fresh-=1
            q.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                    visit.add((r,c))
                if grid[r][c]==1:
                    fresh+=1
        while q and fresh>0:
            for i in range(len(q)):
                r,c= q.popleft()
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            time+=1
        return time if fresh==0 else -1
            

                


