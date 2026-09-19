class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,v in enumerate(tasks):
            v.append(i)
        tasks.sort(key = lambda x: x[0])
        minheap=[]
        res=[]
        time=i=0
        while minheap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minheap,(tasks[i][1],tasks[i][2]))
                i+=1
            if not minheap:
                time=tasks[i][0]
            else:
                curtime,idx= heapq.heappop(minheap)
                time+=curtime
                res.append(idx)
        return res


            
                    







        