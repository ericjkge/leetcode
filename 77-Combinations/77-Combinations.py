# Last updated: 8/17/2025, 10:48:25 PM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(path, start):
            if len(path) == k:
                ans.append(path[:])
                return
            
            for num in range(start, n + 1):
                path.append(num)
                backtrack(path, num + 1)
                path.pop()
        
        backtrack([], 1)
        return ans