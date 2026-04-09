class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[-i for i in nums]
        heapq.heapify(heap)

        for _ in range(k):
            val=heapq.heappop(heap)
        return -val
        
            
        