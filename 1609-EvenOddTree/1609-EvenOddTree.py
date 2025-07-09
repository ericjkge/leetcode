# Last updated: 7/8/2025, 10:59:15 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                if even:
                    node = queue.popleft()
                    if level and node.val <= level[-1] or node.val % 2 == 0:
                        return False
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.popleft()
                    if level and node.val >= level[-1] or node.val % 2 == 1:
                        return False
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            even = not even

        return True