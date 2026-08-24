class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid), len(grid[0])
        minheap=[[grid[0][0],0,0]]
        visit=set()
        visit.add((0,0))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while minheap:
            time,r,c= heapq.heappop(minheap)
            if (r,c)==(rows-1,cols-1):
                return time
            for dr,dc in directions:
                nr,nc= r+dr, c+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                newtime= max(time,grid[nr][nc])
                heapq.heappush(minheap,(newtime, nr,nc))


