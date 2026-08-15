class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        res=[]
        heapq.heapify(minheap)
        for x,y in points:
            dist= x**2 + y**2
            heapq.heappush(minheap,[dist,x,y])
        while minheap and len(res)<k:
            i,j,l= heapq.heappop(minheap)
            res.append([j,l])
        return res