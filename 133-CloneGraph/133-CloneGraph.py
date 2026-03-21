# Last updated: 3/21/2026, 1:53:14 PM
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
11    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
12        if not root:
13            return None
14
15        hashmap = {} # old:new
16
17        def dfs(node):
18            if node in hashmap:
19                return hashmap[node]
20
21            clone = Node(node.val)
22            hashmap[node] = clone
23            
24            for neighbor in node.neighbors:
25                clone.neighbors.append(dfs(neighbor))
26            
27            return clone
28        
29        dfs(root)
30        return hashmap[root]