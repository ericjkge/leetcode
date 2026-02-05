# Last updated: 2/5/2026, 8:49:53 AM
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
13        ans = []
14
15        while queue:
16            n = len(queue)
17            for i in range(n):
18                node = queue.popleft()
19                if node.left:
20                    queue.append(node.left)
21                if node.right:
22                    queue.append(node.right)
23                if i == n - 1:
24                    ans.append(node.val)
25        
26        return ans