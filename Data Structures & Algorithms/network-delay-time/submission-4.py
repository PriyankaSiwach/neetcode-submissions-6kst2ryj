class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap=[(0,k)]
        visit=set()
        t=0
        adj=defaultdict(list)
        for src,dst,j in times:
            adj[src].append((dst,j))

        while minheap:
            dist,node= heapq.heappop(minheap)
            if node in visit:
                continue
            visit.add(node)
            t= max(t,dist)
            for n2,time in adj[node]:
                if n2 not in visit:
                    heapq.heappush(minheap,(dist+time,n2))
        return t if len(visit)==n else -1
                
            
        
            
          
