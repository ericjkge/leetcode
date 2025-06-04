# Last updated: 6/4/2025, 9:39:50 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        mapping = {}

        def dfs(n):
            if n in mapping:
                return mapping[n] # Return copy if it already exists
            
            copy = Node(n.val)

            mapping[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy # Return newly created copy

        return dfs(node) if node else None