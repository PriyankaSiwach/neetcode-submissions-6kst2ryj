class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        prev,recent=0,0
        for i in range(len(nums)-1):
            temp=max(prev+nums[i],recent)
            prev=recent
            recent=temp
        first=recent
        prev,recent=0,0
        for i in range(1,len(nums)):
            temp=max(prev+nums[i],recent)
            prev=recent
            recent=temp
        second=recent
        return max(first,second)
