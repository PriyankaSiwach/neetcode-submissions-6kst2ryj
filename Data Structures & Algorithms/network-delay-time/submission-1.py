class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges= collections.defaultdict(list)
        for root, dest, time in times:
            edges[root].append((dest, time))
        visit=set()
        t=0
        minHeap=[(0,k)]
        while minHeap:
            t1, n1= heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t= max(t,t1)
            for n2, t2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (t1+t2, n2 ))
        return t if len(visit)==n else -1
            
        

        