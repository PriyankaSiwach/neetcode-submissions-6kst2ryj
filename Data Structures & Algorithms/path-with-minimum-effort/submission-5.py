class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols= len(heights), len(heights[0])
        minheap=[[0,0,0]]
        visit=set()
        direction=[[0,1],[0,-1],[1,0],[-1,0]]

        while minheap:
            dist,r,c= heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c)==(rows-1,cols-1):
                return dist
            for dr,dc in direction:
                nr,nc= r+dr, c+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visit:
                    continue
                newdist= max(dist, abs(heights[r][c]-heights[nr][nc]))
                heapq.heappush(minheap,[newdist,nr,nc])

            
            