# Last updated: 7/8/2025, 12:09:11 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node): # True means keep
            if not node:
                return True
            
            if not dfs(node.left):
                node.left = None
            
            if not dfs(node.right):
                node.right = None

            if not node.left and not node.right and node.val == target:
                return False
            return True
        
        dfs(root)
        if not root.left and not root.right and root.val == target:
            return None
        return root