class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        adj={i: [] for i in range(N)}
        for i in range(N):
            x1,y1= points[i]
            for j in range(i+1, N):
                x2,y2=points[j]
                dist= abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        visit=set()
        minHeap=[[0,0]]
        res=0
        while minHeap:
            cost,n = heapq.heappop(minHeap)
            if n in visit:
                continue
            res+=cost
            visit.add(n)
            for cost, nei in adj[n]:
                if nei not in visit:
                    heapq.heappush(minHeap, [cost,nei])
        return res if len(visit)==N else -1

            


    


        