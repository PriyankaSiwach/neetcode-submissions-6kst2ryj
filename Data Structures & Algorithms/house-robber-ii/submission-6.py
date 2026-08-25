class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(s):
            prev,recent=0,0
            for i in s:
                temp=max(prev+i, recent)
                prev=recent
                recent=temp
            return recent
        return max(helper(nums[:-1]), helper(nums[1:]))

            

