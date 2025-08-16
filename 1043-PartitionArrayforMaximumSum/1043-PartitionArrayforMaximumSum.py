# Last updated: 8/16/2025, 11:17:19 PM
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dp(i):
            if i == n:
                return 0
            best = 0
            curr = 0
            for j in range(1, min(k, n - i) + 1):
                curr = max(curr, arr[i + j - 1])
                best = max(best, curr * j + dp(i + j))
            return best
        
        return dp(0)