class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par=[i for i in range(n)]
        rank=[1]* n
        res=n
        def find(n1):
            root=n1
            while root!=par[root]:
                par[root]= par[par[root]]
                root=par[root]
            return par[root]
        def union(n1,n2):
            p1,p2= find(n1), find(n2)
            if p1==p2:
                return 0
            if p1>p2:
                par[p2]=p1
                rank[p1]+=p2
            else:
                par[p1]=p2
                rank[p2]+=p1
            return 1
        for i,j in edges:
            if union(i,j):
                res-=1
        return res



