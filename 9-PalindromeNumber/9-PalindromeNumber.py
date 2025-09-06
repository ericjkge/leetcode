# Last updated: 9/6/2025, 1:47:59 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed = 0

        while x > 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        
        return reversed == original
