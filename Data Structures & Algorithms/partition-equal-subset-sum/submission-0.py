class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp= set()
        dp= {0}
        half= sum(nums)/2
        for i in range(len(nums)):
            tempdp= set()
            for t in dp:
                if t+nums[i]==half:
                    return True
                tempdp.add(t+nums[i])
                tempdp.add(t)
            dp=tempdp
        return True if half in dp else False

        
        