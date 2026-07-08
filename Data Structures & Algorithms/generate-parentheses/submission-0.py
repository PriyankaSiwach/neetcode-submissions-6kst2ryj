class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        sub=[]
        def dfs(open,close):
            if len(sub)==2*n:
                res.append("".join(sub))
                return
            if open<n:
                sub.append("(")
                dfs(open+1,close)
                sub.pop()
            if open>close:
                sub.append(")")
                dfs(open, close+1)
                sub.pop()
            return res
        return dfs(0,0)

           

            