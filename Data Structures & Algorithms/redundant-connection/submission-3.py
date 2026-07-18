class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n+1)]
        rank= [1]*(n+1)

        def find(n1):
            root=n1
            while root!= par[root]:
                par[root]=par[par[root]]
                root=par[root]
            return root
        def union(a,b):
            p1,p2= find(a), find(b)
            if p1==p2:
                return False
            if rank[p2]>rank[p1]:
                par[p1]=par[p2]
                rank[p2]+=rank[p1]
            else:
                par[p2]=par[p1]
                rank[p1]+=rank[p2]
            return True
        for i,j in edges:
            if not union(i,j):
                return [i,j]

        