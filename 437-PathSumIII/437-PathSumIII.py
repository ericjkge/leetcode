# Last updated: 7/8/2025, 12:53:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
            
        counter = 0

        def dfs(node, total):
            nonlocal counter
            if not node:
                return
            
            total += node.val
            if total == targetSum:
                counter += 1
            dfs(node.left, total)
            dfs(node.right, total)

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            dfs(node, 0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return counter