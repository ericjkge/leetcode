# Last updated: 7/8/2026, 12:50:43 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        left = 0
5        ans = 0
6
7        for right in range(len(s)):
8            while s[right] in seen:
9                seen.remove(s[left])
10                left += 1
11
12            seen.add(s[right])
13            ans = max(ans, right - left + 1)
14        
15        return ans