# Last updated: 2/5/2026, 8:48:33 AM
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
16            for _ in range(len(queue) - 1):
17                node = queue.popleft()
18                if node.left:
19                    queue.append(node.left)
20                if node.right:
21                    queue.append(node.right)
22            node = queue.popleft()
23            ans.append(node.val)
24            if node.left:
25                queue.append(node.left)
26            if node.right:
27                queue.append(node.right)
28        
29        return ans