class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        premap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in premap:
                return [premap[diff],i]
            premap[nums[i]]=i
        
        
                