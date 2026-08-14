# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,left,right):
            if not node:
                return True
            if left>= node.val or node.val >= right:
                return False
            leftt= dfs(node.left,left,node.val)
            rightt= dfs(node.right,node.val,right)
            return leftt and rightt
        return dfs(root,float("-inf"), float("inf"))
            



