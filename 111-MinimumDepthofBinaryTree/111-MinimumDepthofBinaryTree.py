# Last updated: 10/22/2025, 10:16:20 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = deque([root])
        min_depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return min_depth + 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            min_depth += 1