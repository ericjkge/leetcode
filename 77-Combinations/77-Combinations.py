# Last updated: 9/2/2025, 8:31:04 AM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(index, path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            for i in range(index, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return ans