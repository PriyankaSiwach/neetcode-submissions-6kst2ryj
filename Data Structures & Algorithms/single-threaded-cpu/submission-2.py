class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,j in enumerate(tasks):
            j.append(i)
        tasks.sort(key= lambda t: t[0])
        minheap, res=[],[]
        i,time=0,tasks[0][0]
        while minheap or i<len(tasks):
            while i <len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not minheap:
                time=tasks[i][0]
            else:
                curtime,index= heapq.heappop(minheap)
                time+=curtime
                res.append(index)
        return res




        
        