# Last updated: 7/9/2025, 8:57:35 PM
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = defaultdict(set)
        for a, sign, _, b in equations:
            if sign == "=":
                graph[a].add(b)
                graph[b].add(a)
        
        seen = set()
        components = defaultdict(int)
        counter = 0

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    components[neighbor] = counter
                    seen.add(neighbor)
                    dfs(neighbor)
        
        for a, _, _, b in equations:
            if a not in seen:
                components[a] = counter
                seen.add(a)
                dfs(a)
            if b not in seen:
                counter += 1
                components[b] = counter
                seen.add(b)
                dfs(b)
            counter += 1
        
        for a, sign, _, b in equations:
            if sign == "!":
                if components[a] == components[b]:
                    return False
        return True
