class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        adj={0:-1}
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            rem =prefix%k
            if rem in adj:
                if i-adj[rem]>=2:
                    return True
            else:
                adj[rem] = i
        return False

