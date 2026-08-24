class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj= defaultdict(list)
        minheap=[(0,src,0)]
        stops=[float("inf")]* n
    
        for i,j,price in flights:
            adj[i].append((j,price))
        while minheap:
            cost,node,flightused= heapq.heappop(minheap)
            if node==dst:
                return cost
            if stops[node]<=flightused:
                continue
            stops[node]=flightused
            if flightused > k:
                continue
        
            for n,p in adj[node]:
                newcost=cost+p
                heapq.heappush(minheap,(newcost,n,flightused+1))
        return -1

        #not optimal
        