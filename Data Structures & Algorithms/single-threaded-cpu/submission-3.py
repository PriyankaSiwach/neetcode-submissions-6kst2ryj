class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,j in enumerate(tasks):
            j.append(i)
        tasks.sort(key= lambda t: t[0])
        heap,res=[],[]
        time=i=0
        
        while heap or i<len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(heap,[tasks[i][1], tasks[i][2]])
                i+=1
            if not heap:
                time=tasks[i][0]
            else:
                curtime,index= heapq.heappop(heap)
                time+=curtime
                res.append(index)
        return res
            
        