class Node:
    def __init__(self):
        self.children={}
        self.endofword=False
class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Node()
            cur= cur.children[c]
        cur.endofword=True

    def search(self, word: str) -> bool:
    
        def dfs(i,root):
            cur=root
            for j in range(i,len(word)):
                c=word[j]
                if c==".":
                    for ch in cur.children.values():
                        if dfs(j+1,ch): return True
                    return False
                if c not in cur.children:
                    return False
                cur=cur.children[c]
            return cur.endofword
        return dfs(0,self.root) 
                
