class Solution:
    def climbStairs(self, n: int) -> int:
        a= [1,1]
        if n<2:
            return a[n]
        for i in range(2,n+1):
            a[0],a[1]=a[1], sum(a)
        return a[1]