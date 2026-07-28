# Last updated: 7/27/2026, 8:34:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11
12        queue = deque([root])
13        vals = []
14
15        while queue:
16            length = len(queue)
17            for i in range(length):
18                node = queue.popleft()
19                if node.left:
20                    queue.append(node.left)
21                if node.right:
22                    queue.append(node.right)
23            
24                if i == length - 1:
25                    vals.append(node.val)
26
27        return vals