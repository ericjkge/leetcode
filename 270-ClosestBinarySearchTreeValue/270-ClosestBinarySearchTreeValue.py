# Last updated: 8/3/2025, 9:13:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest - target) or (abs(root.val - target) == abs(closest - target) and root.val < closest):
                closest = root.val
            if root.val <= target:
                root = root.right
            else:
                root = root.left
        return closest
        