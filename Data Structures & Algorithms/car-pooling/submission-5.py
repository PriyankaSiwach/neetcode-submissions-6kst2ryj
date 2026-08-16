class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minheap=[]
        curpas=0
        for pas,start,end in trips:
            while minheap and minheap[0][0]<=start:
                curpas-=minheap[0][1]
                heapq.heappop(minheap)
            curpas+=pas
            heapq.heappush(minheap,[end,pas])
            if curpas>capacity:
                return False
        return True

        
