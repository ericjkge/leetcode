# Last updated: 1/29/2026, 10:50:59 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        left, right = 0, len(s) - 1
4
5        while left < right:
6            if not s[left].isalnum():
7                left += 1
8                continue
9            
10            if not s[right].isalnum():
11                right -= 1
12                continue
13            
14            if s[left].lower() != s[right].lower():
15                return False
16            
17            left += 1
18            right -= 1
19        
20        return True