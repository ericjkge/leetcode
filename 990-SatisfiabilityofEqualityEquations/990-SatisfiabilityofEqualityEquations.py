# Last updated: 7/9/2025, 5:32:36 PM
from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(list)
        for eq in equations:
            if eq[1:3] == '==':
                a, b = eq[0], eq[3]
                graph[a].append(b)
                graph[b].append(a)

        # DFS to assign component ids
        comp = {}
        curr_id = 0

        def dfs(node):
            comp[node] = curr_id
            for nei in graph[node]:
                if nei not in comp:
                    dfs(nei)

        for var in graph:
            if var not in comp:
                dfs(var)
                curr_id += 1

        # Check "!=" constraints
        for eq in equations:
            if eq[1:3] == '!=':
                a, b = eq[0], eq[3]
                if a == b:
                    return False
                if a in comp and b in comp and comp[a] == comp[b]:
                    return False

        return True
