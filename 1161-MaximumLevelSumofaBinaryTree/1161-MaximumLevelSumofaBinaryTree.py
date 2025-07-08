# Last updated: 7/8/2025, 7:00:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0
        max_sum = -float("inf")
        queue = deque([root])
        counter = 1
        while queue:
            level = 0
            for i in range(len(queue)):
                node = queue.popleft()
                level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(ans, counter)
            if max_sum < level:
                
                ans = counter
                max_sum = level
            counter += 1
        return ans
