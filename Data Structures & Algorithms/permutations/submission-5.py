class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def dfs():
            if len(sub)==len(nums):
                res.append(sub[:])
                return
            for i in nums:
                if i in sub:
                    continue
                sub.append(i)
                dfs()
                sub.pop()
        dfs()
        return res