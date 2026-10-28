class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sub,res=[],[]
        def dfs(start):
            if len(sub)==k:
                res.append(sub[:])
                return
            for i in range(start,n+1):
                if i not in sub:
                    sub.append(i)
                    dfs(i+1)
                    sub.pop()
        dfs(1)
        return res