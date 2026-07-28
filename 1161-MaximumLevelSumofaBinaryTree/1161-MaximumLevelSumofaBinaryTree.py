# Last updated: 7/27/2026, 8:38:50 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        queue = deque([root])
10        mx = float("-inf")
11        ans = None
12
13        count = 1
14        while queue:
15            n = len(queue)
16            level = 0
17            for _ in range(n):
18                node = queue.popleft()
19                if node.left:
20                    queue.append(node.left)
21                if node.right:
22                    queue.append(node.right)
23                level += node.val
24
25            if level > mx:
26                mx = level
27                ans = count
28
29            count += 1
30        
31        return ans