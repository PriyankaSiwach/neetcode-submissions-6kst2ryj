class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        for r in range(1,len(prices)):
            profit= prices[r]-prices[r-1]
            if profit>0:
                maxprofit+=profit
        return maxprofit