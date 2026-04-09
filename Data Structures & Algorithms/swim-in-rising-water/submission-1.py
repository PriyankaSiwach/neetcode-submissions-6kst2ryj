class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols= len(grid), len(grid[0])
        visit=set()
        minHeap=[[grid[0][0], 0,0]]   #time/maxheight, r,c

        def bfs(r,c):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visit:
                return
            visit.add((r,c))
            heapq.heappush(minHeap, [max(t,grid[r][c]), r, c])
            

        while minHeap:
            t,r,c= heapq.heappop(minHeap)
            if r==rows-1 and c==cols-1:
                return t
            bfs(r-1,c)
            bfs(r+1,c)
            bfs(r,c-1)
            bfs(r,c+1)
        
        



        
        