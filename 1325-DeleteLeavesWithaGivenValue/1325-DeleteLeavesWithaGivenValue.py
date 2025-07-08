# Last updated: 7/8/2025, 12:13:27 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # node.val == target and not node.left and not node.right
        def dfs(n):
            if not n:
                return None
            
            n.left = dfs(n.left)
            n.right = dfs(n.right)

            if n.val == target and not n.left and not n.right:
                return None
            
            return n
        return dfs(root)