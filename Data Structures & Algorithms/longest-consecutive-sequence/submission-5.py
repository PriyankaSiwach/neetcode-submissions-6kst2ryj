class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s= set(nums)
        res=0
        for n in nums:
            if n-1 not in s:
                next_n= n+1
                length=1
                while next_n in s:
                    next_n+=1
                    length+=1
                res= max(res,length)
        return res
        
            
            
