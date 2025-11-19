# Last updated: 11/19/2025, 10:56:31 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binExp(b, p):
            if p == 0:
                return 1
            
            if p < 0:
                return 1/binExp(b, -p)
            
            if p % 2 == 1:
                return b * binExp(b * b, (p - 1) / 2)
            return binExp(b * b, p / 2)

        return binExp(x, n)