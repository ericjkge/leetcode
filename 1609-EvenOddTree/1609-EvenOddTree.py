# Last updated: 7/8/2025, 11:03:42 PM
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
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if even:
                    if prev and node.val <= prev or node.val % 2 == 0:
                        return False
                else:
                    if prev and node.val >= prev or node.val % 2 == 1:
                        return False
                
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            even = not even

        return True