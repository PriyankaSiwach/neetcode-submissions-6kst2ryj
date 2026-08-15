class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap=[-n for n in nums]
        heapq.heapify(maxheap)
        while k>0:
            value=heapq.heappop(maxheap)
            k-=1
        return -value
        

