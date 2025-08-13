# Last updated: 8/13/2025, 11:49:49 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1 and n % 3 == 0:
            n //= 3

        return n == 1