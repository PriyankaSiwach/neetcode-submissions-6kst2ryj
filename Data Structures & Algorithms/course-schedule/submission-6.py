class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj= {c:[] for c in range(numCourses)}
        visit=set()
        for n,pre in prerequisites:
            adj[n].append(pre)
        def dfs(course):
            if course in visit:
                return False
            if adj[course]==[]:
                return True
            visit.add(course)
            for nei in adj[course]:
                if not dfs(nei):return False
            visit.remove(course)
            adj[course]=[]
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 

        