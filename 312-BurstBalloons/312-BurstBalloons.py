# Last updated: 8/22/2025, 6:15:17 PM
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)

        @cache
        def dp(i, j): # i, j exclusive
            if i + 1 >= j:
                return 0

            best = 0
            for k in range(i + 1, j):
                best = max(best, arr[i] * arr[k] * arr[j] + dp(i, k) + dp(k, j))
            return best

        return dp(0, n - 1)