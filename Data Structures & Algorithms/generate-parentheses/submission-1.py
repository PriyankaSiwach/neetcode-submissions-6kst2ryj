class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        sub=[]
        def dfs(open,close):
            if len(sub)==n*2:
                res.append("".join(sub[:]))
                return
            if open<n:
                sub.append("(")
                dfs(open+1,close)
                sub.pop()
            if close<open:
                sub.append(")")
                dfs(open,close+1)
                sub.pop()
        dfs(0,0)
        return res
             