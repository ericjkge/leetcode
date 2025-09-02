# Last updated: 9/1/2025, 8:15:45 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        ans = []

        def backtrack(node, path):
            if node == target:
                ans.append(path[:])
                return

            for n in graph[node]:
                    path.append(n)
                    backtrack(n, path)
                    path.pop()

        backtrack(0, [0])
        return ans