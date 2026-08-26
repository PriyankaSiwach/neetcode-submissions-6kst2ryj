class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax,curmin=1,1
        res=max(nums)
        for i in nums:
            if i==0:
                curmax,curmin=1,1
                continue
            temp=curmax
            curmax= max(curmax*i, curmin*i, i)
            curmin= min(temp*i, curmin*i, i)
            res= max(res,curmax)
        return res
