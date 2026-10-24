class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={c:[] for c in range(numCourses)}
        res=[]
        visit,completed=set(), set()
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        def dfs(crs):
            if crs in visit:
                return False
            if crs in completed:
                return True
            visit.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):return False
            visit.remove(crs)
            completed.add(crs)
            res.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

            