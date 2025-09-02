# Last updated: 9/1/2025, 8:14:14 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        seen = set([0])
        ans = []

        def backtrack(node, path):
            if node == target:
                ans.append(path[:])
                return

            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    path.append(n)
                    backtrack(n, path)
                    seen.remove(n)
                    path.pop()

        backtrack(0, [0])
        return ans