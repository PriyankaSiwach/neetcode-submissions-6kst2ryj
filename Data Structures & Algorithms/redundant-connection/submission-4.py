class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par=[i for i in range(n+1)]
        rank=[1]* (n+1)
        def find(n1):
            while n1!=par[n1]:
                par[n1]=par[par[n1]]
                n1=par[n1]
            return n1
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return True
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=rank[p2]
            return False
        for i,j in edges:
            if union(i,j):
                return [i,j]

            