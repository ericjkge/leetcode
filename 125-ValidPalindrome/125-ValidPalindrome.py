# Last updated: 3/20/2026, 3:36:50 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        clean = []
4        for char in s:
5            if char.isalnum():
6                clean.append(char.lower())
7        
8        return clean == clean[::-1]