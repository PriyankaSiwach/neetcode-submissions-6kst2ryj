class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        sub=[]
        def dfs(i):
            if len(sub)==k :
                res.append(sub[:])
                return
            if i>n:
                return
            sub.append(i)
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(1)
        return res

