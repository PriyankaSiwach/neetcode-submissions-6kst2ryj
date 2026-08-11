class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r= max(weights), sum(weights)
        
        def canfinish(cap):
            day,curcap= 1, cap
            for w in weights:
                if curcap-w<0:
                    day+=1
                    curcap=cap
                curcap-=w
            return day<=days
        res= r
        while l<=r:
            mid= (l+r)//2
            if canfinish(mid):
                res= min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
