# Last updated: 7/20/2025, 11:14:28 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(start, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ans
