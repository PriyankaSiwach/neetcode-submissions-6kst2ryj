class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap=[(0,0)]
        visit=set()
        res=0
        n=len(points)
        while len(visit)<n:
            dist,i= heapq.heappop(minheap)
            if i in visit:
                continue
            x1,y1= points[i]
            visit.add(i)
            res+=dist
            for j in range(len(points)):
                x2,y2=points[j]
                if j not in visit:
                    distance= abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(minheap,(distance,j))
        return res



    
        
        