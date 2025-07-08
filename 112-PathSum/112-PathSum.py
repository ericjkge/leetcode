# Last updated: 7/8/2025, 12:35:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = []
        total = 0

        stack.append((root, 0))
        while stack:
            node, total = stack.pop()
            total += node.val
            if not node.left and not node.right and total == targetSum:
                return True
            if node.left:
                stack.append((node.left, total))
            if node.right:
                stack.append((node.right, total))
        return False

        