class Solution:

    def __init__(self, w: List[int]):
        self.prefix=[]
        total=0
        for wei in w:
            total+=wei
            self.prefix.append(total)
        self.total=total

    def pickIndex(self) -> int:
        target=random.randint(1,self.total)
        l,r=0,len(self.prefix)-1
        while l<r:
            m=(l+r)//2
            if self.prefix[m]>=target:
                r=m
            else:
                l=m+1
        return l

        





# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()