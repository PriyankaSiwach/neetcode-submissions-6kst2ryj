class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap,res=[],""
        for cnt,char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if cnt!=0:
                heapq.heappush(maxheap,[cnt,char])
        while maxheap:
            count, char1= heapq.heappop(maxheap)
            if len(res)>1 and char1==res[-1]==res[-2]:
                if not maxheap:
                    break
                count2,char2= heapq.heappop(maxheap)
                count2+=1
                res+=char2
                if count2:
                    heapq.heappush(maxheap,[count2,char2])
            else:
                count+=1
                res+=char1
            if count:
                heapq.heappush(maxheap,[count,char1])
        return res
            
            
        