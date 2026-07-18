class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        visit=set()
        
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        def dfs(i):
            if i in visit:
                return False
            if premap[i]==[]:
                return True
            visit.add(i)
            for nei in premap[i]:
                if not dfs(nei): return False
            visit.remove(i)
            premap[i]=[]
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True
            
