class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        res=[]
        for src,dst in tickets:
            adj[src].append(dst)
        for i in adj:
            adj[i].sort(reverse=True)
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)
        dfs("JFK")
        return res[::-1]
            
            
