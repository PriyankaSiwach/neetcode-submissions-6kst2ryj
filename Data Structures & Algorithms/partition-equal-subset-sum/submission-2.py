class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp= set()
        dp={0}
        half= sum(nums)/2
        for i in range(len(nums)):
            tempdp=set()
            for j in dp:
                if nums[i]+j==half:
                    return True
                tempdp.add(nums[i]+j)
                tempdp.add(j)
            dp=tempdp
        return True if half in dp else False

        