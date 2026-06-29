class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap,res= [],""
        for cnt, char in [(-a,"a"),(-b,"b"), (-c,"c")]:
            if cnt!=0:
                heapq.heappush(maxheap,[cnt,char])
        while maxheap:
            count,char= heapq.heappop(maxheap)
            if len(res)>1 and res[-1]==res[-2]==char:
                if not maxheap:
                    break
                count2, char2= heapq.heappop(maxheap)
                count2+=1
                res+=char2
                if count2:
                    heapq.heappush(maxheap,[count2,char2])
            else:
                count+=1
                res+=char
            if count:
                heapq.heappush(maxheap,[count,char])
        return res


                    

        



        