# Last updated: 2/26/2026, 9:46:40 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        def expand(i, j):
4            while i >= 0 and j < len(s) and s[i] == s[j]:
5                i -= 1
6                j += 1
7            return j - i - 1
8    
9        ans = ""
10        for i in range(len(s)):
11            even = expand(i, i + 1)
12            if even > len(ans):
13                half = even // 2
14                ans = s[i - half + 1:i + half + 1]
15            odd = expand(i, i)
16            if odd > len(ans):
17                half = odd // 2
18                ans = s[i - half:i + half + 1]
19        
20        return ans
21
22
23