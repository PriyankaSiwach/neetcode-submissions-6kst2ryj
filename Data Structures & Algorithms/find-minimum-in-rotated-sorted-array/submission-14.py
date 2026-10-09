class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0, len(nums)-1
        res=nums[0]
        if nums[l]<nums[r]:
            return nums[l]
        while l<=r:
            m= (l+r)//2
            if nums[m]>=nums[l]:
                res= min(res,nums[l])
                l=m+1
            else:
                res= min(res,nums[m])
                r=m-1
        return res


