class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def dfs(i):
            if i >=len(nums):
                res.append(sub[:])
                return 
            sub.append(nums[i])
            dfs(i+1)
            sub.remove(nums[i])
            dfs(i+1)
            return res
        return dfs(0)