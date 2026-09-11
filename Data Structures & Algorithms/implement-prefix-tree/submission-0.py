class Node:
    def __init__(self):
        self.children={}
        self.endofword=False
class PrefixTree:

    def __init__(self):
        self.root= Node()

    def insert(self, word: str) -> None:
        cur= self.root
        for i in word:
            if i not in cur.children:
                cur.children[i]=Node()
            cur= cur.children[i]
        cur.endofword=True

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.endofword
    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True





        