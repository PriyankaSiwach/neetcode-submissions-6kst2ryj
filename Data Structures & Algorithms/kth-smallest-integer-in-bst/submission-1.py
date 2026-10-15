# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.minheap=[]
        def dfs(root):
            if not root:
                return None
            left= dfs(root.left)
            heapq.heappush(self.minheap,root.val)
            right=dfs(root.right)
            return root
        dfs(root)
        while self.minheap and k>1:
            heapq.heappop(self.minheap)
            k-=1
        return self.minheap[0]

