class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap=[(0,k)]
        visit= set()
        adj= defaultdict(list)
        time=0
        for sr,dst, t in times:
            adj[sr].append((t,dst))
        while minheap:
            t1,n1= heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            time=t1
            for t2,nei in adj[n1]:
                if nei not in visit:
                    heapq.heappush(minheap,(time+t2,nei))
        return time if len(visit)==n else -1


            