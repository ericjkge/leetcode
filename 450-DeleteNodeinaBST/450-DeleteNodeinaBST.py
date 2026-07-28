# Last updated: 7/28/2026, 4:42:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
9        if not root:
10            return None
11
12        if root.val > key:
13            root.left = self.deleteNode(root.left, key)
14        elif root.val < key:
15            root.right = self.deleteNode(root.right, key)
16        else:
17            if root.left and root.right:
18                prev = root
19                cur = root.right
20                while cur.left is not None:
21                    prev = cur
22                    cur = cur.left
23                
24                if prev != root:
25                    prev.left = cur.right
26                    cur.right = root.right
27                    
28                cur.left = root.left
29                return cur
30            elif root.left:
31                return root.left
32            elif root.right:
33                return root.right
34            else:
35                return None
36
37        return root
38