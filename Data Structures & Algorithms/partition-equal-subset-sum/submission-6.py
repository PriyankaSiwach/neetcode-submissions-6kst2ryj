class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp=set()
        dp={0}
        half= sum(nums)/2
        for i in range(len(nums)):
            temp=set()
            for j in dp:
                if j+nums[i]==half:
                    return True
                temp.add(nums[i]+j)
                temp.add(j)
            dp=temp
        return True if half in dp else False

        