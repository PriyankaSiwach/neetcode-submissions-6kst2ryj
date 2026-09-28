"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        res= set()
        cur=p
        while cur:
            res.add(cur)
            cur= cur.parent
        cur=q
        while cur:
            if cur in res:
                return cur
            cur= cur.parent