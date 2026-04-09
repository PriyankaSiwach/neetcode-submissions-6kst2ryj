class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        PreMap={x:[] for x in range(numCourses)}
        res=[]
        cycle,visit= set(),set()
        for crs,pre in prerequisites:
            PreMap[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
           
            for pre in PreMap[crs]:
                if not dfs(pre): 
                    return False
            cycle.remove(crs)
           
            res.append(crs)
            visit.add(crs)
            return True
        for crs in range (numCourses):
            if not dfs(crs): return []
        return res


        