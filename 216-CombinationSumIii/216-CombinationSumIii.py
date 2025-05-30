# Last updated: 5/30/2025, 12:07:58 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, start):
            if len(curr) == k:
                if sum(curr) == n:
                    ans.append(curr[:])
                return
            
            for i in range(start, 10):
                if sum(curr) + i <= n:
                    curr.append(i)
                    backtrack(curr, i + 1)
                    curr.pop()
        
        ans = []
        backtrack([], 1)
        return ans