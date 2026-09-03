class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj={i:[] for i in range(n)}
        q= deque([0])
        visit=set()
        visit.add(0)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        while q:
            node= q.popleft()
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
        return len(visit)==n



