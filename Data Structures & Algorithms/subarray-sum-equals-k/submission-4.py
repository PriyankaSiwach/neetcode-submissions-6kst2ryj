class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash={0:1}
        prefix=0
        res=0
        for i in range(len(nums)):
            prefix+=nums[i]
            diff= prefix-k
            if diff in hash:
                res+=hash[diff] #old value needs to be removed has seen it!
            hash[prefix]= 1+ hash.get(prefix,0) # new sum i just created
        return res
