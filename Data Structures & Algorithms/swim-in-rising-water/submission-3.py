class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N= len(grid)
        visit=set()
        visit.add((0,0))
        minheap=[[grid[0][0], 0,0]]
        directions= [[0,1], [0,-1], [1,0], [-1,0]]
        while minheap:
            time, row, col= heapq.heappop(minheap)
            if row==N-1 and col==N-1:
                return time
            
            for dr, dc in directions:
                rows, cols= dr+row, dc+col
                if rows<0 or cols<0 or rows==N or cols==N or (rows,cols) in visit:
                    continue
                visit.add((rows,cols))
                heapq.heappush(minheap, [max(time, grid[rows][cols]), rows, cols])
         


        
        


        


        
        