class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]
        def dfs(i,cursum):
            if cursum==target:
                res.append(sub[:])
                return
            if cursum>target or i>=len(nums):
                return
            sub.append(nums[i])
            dfs(i,nums[i]+cursum)
            sub.pop()
            dfs(i+1,cursum)
        dfs(0,0)
        return res

        