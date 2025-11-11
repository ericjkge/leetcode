# Last updated: 11/11/2025, 9:36:00 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []

        def backtrack(index, path):
            if sum(path) > target:
                return
            
            if sum(path) == target:
                self.ans.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return self.ans

        [1, 1, 2, 5, 6, 7, 10]