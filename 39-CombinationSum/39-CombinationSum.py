# Last updated: 11/11/2025, 9:22:09 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []

        def backtrack(index, path):
            if sum(path) > target:
                return

            if sum(path) == target:
                self.ans.append(path[:])
                return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop() 

        backtrack(0, [])
        return self.ans