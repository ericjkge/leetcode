# Last updated: 11/19/2025, 9:30:13 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binExp(base, power):
            if power == 0:
                return 1

            if power < 0:
                return 1 / binExp(base, -power)
            if power % 2 == 1:
                return base * binExp(base * base, (power - 1) / 2)
            return binExp(base * base, power / 2)

        return binExp(x, n)