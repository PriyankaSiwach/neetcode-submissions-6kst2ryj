class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]
        candidates.sort()
        def dfs(i,cursum):
            if cursum==target:
                res.append(sub[:])
                return
            if cursum>target or i>=len(candidates):
                return
            sub.append(candidates[i])
            dfs(i+1,candidates[i]+cursum)
            sub.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,cursum)
        dfs(0,0)
        return res

