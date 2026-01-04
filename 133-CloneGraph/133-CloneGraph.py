# Last updated: 1/4/2026, 9:54:50 AM
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
15        hashmap = {node: Node(node.val)}
16        
17        def dfs(n):
18            for neighbor in n.neighbors:
19                if neighbor not in hashmap:
20                    clone = Node(neighbor.val)
21                    hashmap[neighbor] = clone
22                    dfs(neighbor)
23                hashmap[n].neighbors.append(hashmap[neighbor])
24
25        dfs(node)
26        return hashmap[node]