class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols= len(heights), len(heights[0])
        visit=set()
        minheap=[[0,0,0]]
        directions= [[1,0], [-1,0], [0,1], [0,-1]]

        while minheap:
            diff,r,c= heapq.heappop(minheap)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c)==(rows-1, cols-1):
                return diff
            for dr,dc in directions:
                nr,nc= r+dr, c+dc
                if nr<0 or nc<0 or nr>=rows or nc>=cols or (nr,nc) in visit:
                    continue
                neweffort= max(diff,abs(heights[r][c]-heights[nr][nc]))
                heapq.heappush(minheap,[neweffort,nr,nc])
                




        