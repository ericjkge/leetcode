# Last updated: 1/14/2026, 10:50:22 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        n = len(s)
4        window = set()
5        left, right = 0, 0
6        longest = 0
7
8        while right < n:
9            while s[right] in window:
10                window.remove(s[left])
11                left += 1
12            window.add(s[right])    
13            longest = max(longest, right - left + 1)
14            right += 1
15        
16        return longest
17