class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target=sum(nums)//k
        if sum(nums)%k!=0:
            return False
        used=[False]* len(nums)
        def dfs(i,k,cursum):
            if k==0:
                return True
            if cursum==target:
                return dfs(0,k-1,0)
            for j in range(i,len(nums)):
                if used[j] or cursum+nums[j]>target:
                    continue
                used[j]=True
                if dfs(j+1,k,cursum+nums[j]):
                    return True
                used[j]=False
            return False
        return dfs(0,k,0)




