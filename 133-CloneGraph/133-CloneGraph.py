# Last updated: 6/8/2025, 6:09:10 PM
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
        if not node:
            return None

        hashmap = defaultdict()
        def dfs(n):
            if hashmap.get(n, 0) != 0:
                return hashmap[n]
            
            new_node = Node(n.val)
            hashmap[n] = new_node
            for neighbor in n.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        
        dfs(node)
        return hashmap[node]