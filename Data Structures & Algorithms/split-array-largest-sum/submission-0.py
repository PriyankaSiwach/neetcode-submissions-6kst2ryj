class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums), sum(nums)
        res=r

        def cansplit(largest):
            subarray=0
            cursum=0
            for i in nums:
                cursum+=i
                if cursum>largest:
                    subarray+=1
                    cursum=i
            return subarray+1<=k

        while l<=r:
            mid= l+ ((r-l)//2)
            if cansplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        
                    
        