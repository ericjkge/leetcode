# Last updated: 12/1/2025, 10:37:43 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11
12        ans = []
13        queue = deque([root])
14        
15        while queue:
16            level = []
17            for _ in range(len(queue)):
18                node = queue.popleft()
19                level.append(node.val)
20                if node.left:
21                    queue.append(node.left)
22                if node.right:
23                    queue.append(node.right)
24            ans.append(level)
25        
26        return ans