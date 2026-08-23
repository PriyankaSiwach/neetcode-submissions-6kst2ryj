class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        edges={}
        leaves=deque()
        for i,k in adj.items():
            if len(k)==1:
                leaves.append(i)
            edges[i]=len(k)
        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                v= leaves.popleft()
                n-=1
                for nei in adj[v]:
                    edges[nei]-=1
                    if edges[nei]==1:
                        leaves.append(nei)
                        
        