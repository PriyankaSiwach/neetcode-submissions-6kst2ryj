class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap= {i:[] for i in range(numCourses)}
        visit=set()
        done=set()
        res=[]

        for crs,pre in prerequisites:
            premap[crs].append(pre)

        def dfs(i):
            if i in visit:
                return False
            if i in done:
                return True
            visit.add(i)
            for nei in premap[i]:
                if not dfs(nei): return False
            visit.remove(i)
            done.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i): return []
        return res

            