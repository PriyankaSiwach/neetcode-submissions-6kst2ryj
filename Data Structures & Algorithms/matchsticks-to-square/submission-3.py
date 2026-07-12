class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total= sum(matchsticks)
        sides=[0]*4
        edge= total//4
        if total % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if sides[j]+matchsticks[i]<=edge:
                    sides[j]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return dfs(0)
