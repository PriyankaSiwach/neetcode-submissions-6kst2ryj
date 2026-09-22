class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        adj={0:1}
        cursum=0
        res=0
        for n in nums:
            cursum+=n
            diff=cursum-k
            if diff in adj:
                res+=adj[diff]
            adj[cursum]= 1+ adj.get(cursum,0)
        return res


