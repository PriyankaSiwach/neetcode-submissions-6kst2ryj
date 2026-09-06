class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        adj={0:1}
        res=0
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            diff= prefix-k
            if diff in adj:
                res+=adj[diff]
            adj[prefix]= 1+ adj.get(prefix,0)
        return res
