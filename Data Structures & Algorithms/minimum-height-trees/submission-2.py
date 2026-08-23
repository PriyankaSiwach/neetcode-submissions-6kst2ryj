class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj=defaultdict(list)
        for i, neigh in edges:
            adj[i].append(neigh)
            adj[neigh].append(i)
        edges= {}
        leaves=deque()
        for i,neigh in adj.items():
            if len(neigh)==1:
                leaves.append(i)
            edges[i]=len(neigh)
                     
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

