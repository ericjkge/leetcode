# Last updated: 7/9/2025, 1:03:46 AM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        
        indegree = [0] * n
        outdegree = [0] * n

        for a, b in trust:
            indegree[b - 1] += 1
            outdegree[a - 1] += 1
        
        for i in range(1, n + 1):
            if indegree[i - 1] == n - 1 and outdegree[i - 1] == 0:
                return i
        
        return -1