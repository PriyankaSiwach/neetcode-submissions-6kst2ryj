class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap= {i: [] for i in range(numCourses)}
        visit=set()
        done=set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if crs in done:
                return True
            visit.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            done.add(crs)
            return True
            
        for i in range(numCourses):
            if not dfs(i): return False
        return True

        
    
        


        