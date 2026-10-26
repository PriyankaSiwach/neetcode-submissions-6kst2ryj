class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n= len(edges)+1
        par=[i for i in range(n)]
        rank=[1]*n
        def find(root):
            while root!=par[root]:
                par[root]=par[par[root]]
                root= par[root]
            return root
        def union(n1,n2):
            p1,p2= find(n1), find(n2)
            if p1==p2:
                return False
            elif rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        res=[]
        for i,j in edges:
            if not union(i,j):
                res=[i,j]
        return res