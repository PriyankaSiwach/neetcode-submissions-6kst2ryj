class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        res=[]
        heapq.heapify(minheap)
        for x,y in points:
            distance= x**2+y**2
            heapq.heappush(minheap,[distance,x,y])
        while minheap and len(res)<k:
            dist,i,j=heapq.heappop(minheap)
            res.append([i,j])
        return res