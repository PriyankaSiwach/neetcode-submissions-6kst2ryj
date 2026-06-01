class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        reslen=float("inf")
        cursum=0
        
        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                reslen= min(reslen, r-l+1)
                cursum-=nums[l]
                l+=1
        return 0 if reslen == float("inf") else reslen
            
        