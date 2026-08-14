# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node,target):
            if not node:
                return None
            if not node.left or not node.right:
                if node.val==target:
                    return None
            node.left= dfs(node.left,target)
            node.right=dfs(node.right,target)
            return node
        return dfs(root,target)