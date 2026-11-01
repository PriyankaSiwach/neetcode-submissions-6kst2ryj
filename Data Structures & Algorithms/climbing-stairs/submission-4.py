class Solution:
    def climbStairs(self, n: int) -> int:
        prev,next= 1,1
        for i in range(n-1):
            temp=next
            next=next+prev
            prev=temp
        return next