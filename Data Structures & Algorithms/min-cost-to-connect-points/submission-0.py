class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        totalcost=0
        minHeap=[(0,0)]
        visit=set()

        while len(visit)<n:
            cost, i= heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            totalcost+=cost
            xi,yi= points[i]

            for j in range(n):
                if j not in visit:
                    xj,yj= points[j]
                    dist= abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(minHeap, (dist, j))
        return totalcost


        