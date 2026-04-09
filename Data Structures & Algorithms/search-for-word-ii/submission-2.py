class Node:
    def __init__(self):
        self.children={}
        self.endofWord=False
    def addWord(self, w):
        cur= self
        for c in w:
            if c not in cur.children:
                cur.children[c]=Node()
            cur=cur.children[c]
        cur.endofWord= True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Node()
        for w in words:
            root.addWord(w)
        rows, cols= len(board), len(board[0])
        res, path= set(), set()
        def dfs(r,c,node, word):
            
            if (r<0 or c<0 or r==rows or c==cols or board[r][c] not in node.children or (r,c) in path):
                return False
            path.add((r,c))
            node= node.children[board[r][c]]
            word+=board[r][c]
            if node.endofWord:
                res.add(word)
            dfs(r+1, c, node, word) 
            dfs(r-1,c, node, word) 
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            path.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, root, "")
        return list(res)


        
       

        