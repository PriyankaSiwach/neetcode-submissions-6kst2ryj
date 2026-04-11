class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, recent= 0,0
        for i in nums:
            temp= max(prev+i, recent)
            prev=recent
            recent= temp
        return recent
    