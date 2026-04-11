class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices= [float("inf")]*n
        prices[src]=0
        for i in range(k+1):
            temp=prices[:]
            for s,d, t in flights:
                if prices[s]==float("inf"):
                    continue
                if prices[s]+t<temp[d]:
                    temp[d]=prices[s]+t
            prices=temp
        return -1 if prices[dst] ==float("inf") else prices[dst]
            

        
            

            
       

        