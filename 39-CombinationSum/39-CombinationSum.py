# Last updated: 6/28/2025, 7:00:37 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(total, path, start):
            if total == target:
                ans.append(path[:])
                return
            
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(total + candidates[i], path, i)
                path.pop()
        
        backtrack(0, [], 0)
        return ans