# Last updated: 7/9/2025, 4:22:48 PM
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        self.ans = 0
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        
        def dfs(node, total):
            if not graph[node]:
                self.ans = max(self.ans, total)

            for child in graph[node]:
                dfs(child, total + informTime[node])
        
        dfs(headID, 0)
        return self.ans