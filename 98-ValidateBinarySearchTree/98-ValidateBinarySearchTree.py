# Last updated: 9/11/2025, 12:59:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tree = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)
        
        dfs(root)

        for i in range(len(tree)):
            if i and tree[i] <= tree[i - 1]:
                return False
        return True