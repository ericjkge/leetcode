# Last updated: 9/2/2025, 8:37:53 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def backtrack(index, path):
            if sum(path) > target:
                return
            
            if sum(path) == target:
                ans.append(path[:])
            
            for i in range(index, n):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, [])
        return ans