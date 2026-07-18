class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par= [i for i in range(n)]
        rank=[1]*n
        def find(n1):
            root=n1
            while root!=par[root]:
                par[root]=par[par[root]]
                root=par[root]
            return root
        def union(a,b):
            p1,p2= find(a), find(b)
            if p1==p2:
                return 0
            if rank[p2]>rank[p1]:
                par[p1]=par[p2]
                rank[p2]+=rank[p1]
            else:
                par[p2]=par[p1]
                rank[p1]+=rank[p2]
            return 1
        res=n
        for i,j in edges:
            res-=union(i,j)
        return res

           
        
            
            
