class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            prev= cost[i]+cost[i+2]
            next=cost[i]+cost[i+1]
            cost[i]= min(prev,next)
        return min(cost[0],cost[1])





