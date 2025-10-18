# Last updated: 10/18/2025, 11:32:13 AM
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
            
        hashmap = {node:Node(node.val)}

        queue = deque([node])
        while queue:
            n = queue.popleft()
            print(n.val)
            c = hashmap[n]
            for neighbor in n.neighbors:
                if neighbor not in hashmap:
                    copy = Node(neighbor.val)
                    hashmap[neighbor] = copy
                    queue.append(neighbor)
                c.neighbors.append(hashmap[neighbor])
        
        return hashmap[node]