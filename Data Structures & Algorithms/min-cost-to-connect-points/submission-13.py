class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap=[[0,0]]
        visit=set()
        res=0
        n= len(points)
        while len(visit)<n:
            if minheap:
                cost,i= heapq.heappop(minheap)
            if i in visit:
                continue
            visit.add(i)
            res+=cost
            x,y= points[i]
            for j in range(n):
                if j not in visit:
                    x2,y2=points[j]
                    dist= abs(x-x2)+abs(y-y2)
                    heapq.heappush(minheap,[dist,j])
        return res
