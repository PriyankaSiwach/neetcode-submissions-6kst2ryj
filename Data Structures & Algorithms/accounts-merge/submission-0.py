class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[1]*n
    def find(self,n1):
        root=n1
        while self.par[root]!=root:
            self.par[root]=self.par[self.par[root]]
            root=self.par[root]
        return root
    def union(self,a,b):
        p1,p2=self.find(a), self.find(b)
        if p1==p2:
            return False
        if self.rank[p2]>self.rank[p1]:
            self.par[p1]=self.par[p2]
            self.rank[p2]+=self.rank[p1]
        else:
            self.par[p2]=self.par[p1]
            self.rank[p1]+=self.rank[p2]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf= UnionFind(len(accounts))
        emailtoAcc={}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoAcc:
                    uf.union(i,emailtoAcc[e])
                else:
                    emailtoAcc[e]=i
        emailGroup=defaultdict(list)
        for e, i in emailtoAcc.items():
            leader= uf.find(i)
            emailGroup[leader].append(e)
        res=[]
        for i,e in emailGroup.items():
            name= accounts[i][0]
            res.append([name]+ sorted(emailGroup[i]))
        return res








    