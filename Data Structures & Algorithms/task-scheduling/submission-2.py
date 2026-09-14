class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count= Counter(tasks)
        maxheap=[-c for c in count.values()]
        q=deque()
        t=0
        heapq.heapify(maxheap)
        while maxheap or q:
            t+=1
            if maxheap:
                cnt= heapq.heappop(maxheap)
                cnt+=1
                if cnt:
                    q.append([cnt,t+n])
            if q and q[0][1]==t:
                val,time= q.popleft()
                heapq.heappush(maxheap,val)
        return t

            



        