# Last updated: 9/15/2025, 12:39:55 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)

        dfs(root)
        return tree[k - 1]