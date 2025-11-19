# Last updated: 11/19/2025, 9:21:07 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        return x * pow(x, n - 1)