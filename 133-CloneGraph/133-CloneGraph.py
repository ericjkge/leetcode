# Last updated: 6/4/2025, 9:27:29 AM
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
        
        graph_map = {}
        graph_map[node] = Node(node.val)

        def dfs(n):
            for neighbor in n.neighbors:
                if neighbor not in graph_map.keys():
                    graph_map[neighbor] = Node(neighbor.val)
                    dfs(neighbor)
                graph_map[n].neighbors.append(graph_map[neighbor])

        dfs(node)


        return graph_map[node]