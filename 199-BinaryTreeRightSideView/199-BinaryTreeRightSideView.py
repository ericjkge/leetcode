# Last updated: 12/26/2025, 11:03:21 PM
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
12        ans = []
13        queue = deque([root])
14        while queue:
15            n = len(queue)
16            for i in range(n):
17                node = queue.popleft()
18                if node.left:
19                    queue.append(node.left)
20                if node.right:
21                    queue.append(node.right)
22                if i == n - 1:
23                    ans.append(node.val)
24        
25        return ans
26            