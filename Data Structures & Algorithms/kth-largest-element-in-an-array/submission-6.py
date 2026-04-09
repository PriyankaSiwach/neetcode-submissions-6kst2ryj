class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #using max heap
        heap=[-i for i in nums]
        heapq.heapify(heap)

        while k>0:
            val=heapq.heappop(heap)
            k-=1
        return -val

        # minheap=[]

        # for n in nums:
        #     heapq.heappush(minheap,n)
        #     if len(minheap)>k:
        #         heapq.heappop(minheap)
        # return minheap[0]

        
            
        