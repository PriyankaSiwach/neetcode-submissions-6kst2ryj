class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total= sum(nums)
        target= total//k
        used=[False]*len(nums)
        if total%k!=0:
            return False
        def backtrack(i,k,cursum):
            if k==0:
                return True
            if cursum==target:
                return backtrack(0,k-1,0)
            for j in range(i,len(nums)):
                if used[j] or cursum+ nums[j]>target:
                    continue
                used[j]=True
                if backtrack(j+1,k,cursum+nums[j]):
                    return True
                used[j]=False
            return False
        return backtrack(0,k,0)
