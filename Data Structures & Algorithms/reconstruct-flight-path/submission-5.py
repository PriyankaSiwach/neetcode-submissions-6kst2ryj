class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj= collections.defaultdict(list)
        for src, des in tickets:
            adj[src].append(des)
        for src in adj:
            adj[src].sort(reverse=True)
        res=[]
        def dfs(src):
            while adj[src]:
                value=adj[src].pop()
                dfs(value)
            res.append(src)
        dfs("JFK")
        return res[::-1]

        