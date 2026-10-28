class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sub,res=[],[]
        total=n*2
        def dfs(open,close):
            if len(sub)==total:
                res.append("".join(sub))
                return
            if open<n:
                sub.append("(")
                dfs(open+1,close)
                sub.pop()
            if open>close:
                sub.append(")")
                dfs(open,close+1)
                sub.pop()
        dfs(0,0)
        return res

            
