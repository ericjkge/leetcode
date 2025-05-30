# Last updated: 5/30/2025, 12:07:45 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        ans = []
        def backtrack(curr, path):
            if curr == end:
                ans.append(path[:])
                return
            
            for neighbor in graph[curr]:
                path.append(neighbor)
                backtrack(neighbor, path)
                path.pop()
                
        path = [0]
        backtrack(0, path)
        return ans