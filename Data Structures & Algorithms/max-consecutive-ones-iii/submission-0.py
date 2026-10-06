class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        one=0
        l=0
        res=0
        for r in range(len(nums)):
            c=nums[r]
            if c==1:
                one+=1
            if (r-l+1)-one>k:
                if nums[l]==1:
                    one-=1
                l+=1
            else:
                res= max(res,(r-l+1))
        return res