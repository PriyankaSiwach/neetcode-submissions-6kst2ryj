class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c :set() for w in words for c in w}
        visit={}
        res=[]
        for i in range(len(words)-1):
            w1,w2= words[i],words[i+1]
            minlen= min(len(w1), len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for i in range(minlen):
                if w1[i]!=w2[i]:
                    adj[w1[i]].add(w2[i])
                    break
        def dfs(i):
            if i in visit:
                return visit[i]
            visit[i]=True
            for nei in adj[i]:
                if dfs(nei):
                    return True
            visit[i]=False
            res.append(i)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

