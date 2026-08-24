class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj= defaultdict(list)
        n=len(points)
        for i in range(n):
            x1,y1= points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist= abs(x1-x2)+abs(y1-y2)
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        minheap=[(0,0)]
        res=0
        visit=set()
        while minheap:
            cost,n1= heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            res+=cost
            for c,nei in adj[n1]:
                if nei not in visit:
                    heapq.heappush(minheap,(c,nei))
            # res+=cost
        return res if len(visit)==n else -1
                

            