# Last updated: 8/13/2025, 11:47:07 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n:
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            n //= 3

        return False