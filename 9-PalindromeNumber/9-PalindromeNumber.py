# Last updated: 11/14/2025, 9:52:29 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num = x
        palindrome = 0
        while num > 0:
            palindrome = palindrome * 10 + num % 10
            num //= 10
        
        return palindrome == x