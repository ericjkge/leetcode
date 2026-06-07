# Last updated: 6/7/2026, 11:29:52 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
9        children = {child for _, child, _ in descriptions}
10        root = next(p for p, _, _ in descriptions if p not in children)
11        mapping = {}
12
13        for p, c, l in descriptions:
14            if p not in mapping:
15                mapping[p] = TreeNode(val=p)
16            
17            if c not in mapping:
18                mapping[c] = TreeNode(val=c)
19
20            if l == 1:
21                mapping[p].left = mapping[c]
22            else:
23                mapping[p].right = mapping[c]
24        
25        return mapping[root]