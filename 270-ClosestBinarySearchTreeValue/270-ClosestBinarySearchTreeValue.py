# Last updated: 5/30/2025, 12:07:57 PM
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
            curr = abs(target - root.val)
            past = abs(target - closest)
            
            if curr < past or (curr == past and root.val < closest):
                closest = root.val
            
            if target < root.val:
                root = root.left
            else:
                root = root.right
        
        return closest
            
        