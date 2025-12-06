# Last updated: 12/6/2025, 10:31:11 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        n = len(s)
4        left, right = 0, n - 1
5
6        while left < right:
7            if not s[left].isalnum():
8                left += 1
9                continue
10            elif not s[right].isalnum():
11                right -= 1
12                continue
13            else:
14                if s[left].lower() != s[right].lower():
15                    return False
16                else:
17                    left += 1
18                    right -= 1
19        
20        return True