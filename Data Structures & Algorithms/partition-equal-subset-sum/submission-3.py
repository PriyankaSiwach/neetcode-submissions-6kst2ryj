class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half=sum(nums)/2
        dp=set()
        dp={0}
        for i in range(len(nums)):
            temp=set()
            for j in dp:
                if j+nums[i]==half:
                    return True
                temp.add(j+nums[i])
                temp.add(j)
            dp=temp
        return True if half in dp else False 

