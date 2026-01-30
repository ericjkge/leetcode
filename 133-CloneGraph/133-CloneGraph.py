# Last updated: 1/30/2026, 10:02:17 AM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        if not node:
13            return None
14            
15        mapping = {} # original : clone
16        
17        def dfs(n):
18            if n in mapping:
19                return mapping[n]
20            
21            clone = Node(n.val)
22            mapping[n] = clone
23
24            for neighbor in n.neighbors:
25                clone.neighbors.append(dfs(neighbor))
26
27            return clone
28
29        return dfs(node)