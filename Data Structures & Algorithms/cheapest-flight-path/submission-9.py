class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices= [float("inf")]* n
        prices[src]=0

        for i in range(k+1):
            temp=prices[:]
            for src, des, time in flights:
                if prices[src]==float("inf"):
                    continue
                if prices[src]+time< temp[des]:
                    temp[des]=prices[src]+time
            prices=temp
        return -1 if prices[dst]==float("inf") else prices[dst]
            

            
       

        