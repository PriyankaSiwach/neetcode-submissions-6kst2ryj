class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        l,r=1,x
        while l<=r:
            m=(l+r)//2
            if m*m > x:
                r=m-1
            elif m*m<x:
                ans=m
                l=m+1
            elif m*m==x:
                return m
        return ans


        