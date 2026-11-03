# Last updated: 11/3/2026, 12:29:24 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: TreeNode | None) -> int:
9        queue = deque([root])
10        smallest = None
11        maximum = None
12        level = 0
13
14        while queue:
15            level += 1
16            size = len(queue)
17            total = 0
18            for _ in range(size):
19                node = queue.popleft()
20                total += node.val
21                if node.left:
22                    queue.append(node.left)
23                if node.right:
24                    queue.append(node.right)
25            if maximum is None or total > maximum:
26                smallest = level
27                maximum = total
28        
29        return smallest