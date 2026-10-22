"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew={}
        def dfs(realnode):
            if realnode in oldtonew:
                return oldtonew[realnode]
            copynode= Node(realnode.val)
            oldtonew[realnode]=copynode
            for nei in realnode.neighbors:
                copynode.neighbors.append(dfs(nei))
            return copynode
        return dfs(node) if node else None
            
