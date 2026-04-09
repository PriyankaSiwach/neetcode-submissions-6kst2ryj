class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=collections.defaultdict(list)
        res=[]
        for src, dest, in tickets:
            adj[src].append(dest)
            for src in adj:
                adj[src].sort(reverse=True)
        def dfs(src):
            while adj[src]:
                value=adj[src].pop()
                dfs(value)
            res.append(src)
        dfs("JFK")
        return res[::-1]
    

        