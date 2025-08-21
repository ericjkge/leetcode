# Last updated: 8/22/2025, 12:19:02 AM
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)

        @cache
        def dp(i, j):
            if i == j:
                return 0

            smallest = float("inf")
            for k in range(i, j):
                smallest = min(smallest, max(arr[i:k + 1]) * max(arr[k + 1:j + 1]) + dp(i, k) + dp(k + 1, j))
            return smallest

        return dp(0, n - 1)