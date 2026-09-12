class Node:
    def __init__(self):
        self.children={}
        self.end=False
class Trie:
    def __init__(self,words):
        self.root=Node()
    def addword(self,word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Node()
            cur=cur.children[c]
        cur.end=True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie(words)
        rows,cols= len(board), len(board[0])
        path,res= set(),set()
        for i in words:
            trie.addword(i)
        root=trie.root
        def dfs(r,c, node, word):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c] not in node.children or (r,c) in path:
                return 
            path.add((r,c))
            node= node.children[board[r][c]]
            word+=board[r][c]
            if node.end:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            path.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)









