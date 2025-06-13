# Last updated: 6/13/2025, 12:53:22 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.counter = 0
        def backtrack(target, path, start):
            if target == 0:
                ans.append(path[:])
                return
    
            elif target < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(target - candidates[i], path, i)
                path.pop()
        
        backtrack(target, [], 0)
        return ans
