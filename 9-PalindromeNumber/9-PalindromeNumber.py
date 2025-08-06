# Last updated: 8/7/2025, 12:00:05 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reversed = 0
        
        while x > 0:
            reversed = reversed * 10 + x % 10
            x //= 10
            
        return reversed == original