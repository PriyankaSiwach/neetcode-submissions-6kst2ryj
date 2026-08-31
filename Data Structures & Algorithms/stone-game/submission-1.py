class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp={}
        def dfs(i,j):
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            left= piles[i]- dfs(i+1,j)
            right=piles[j] - dfs(i,j-1)
            dp[(i,j)]= max(left,right)
            return dp[(i,j)]
        return dfs(0,len(piles)-1)>0
        