class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        reslen=float("inf")
        cursum=0
        
        for r in range(len(nums)):
            cursum+=nums[r]
            while cursum>=target:
                newlen= r-l+1
                reslen= min(reslen, newlen)
                cursum-=nums[l]
                l+=1
        if reslen == float("inf"):
            return 0
        return reslen
            
        