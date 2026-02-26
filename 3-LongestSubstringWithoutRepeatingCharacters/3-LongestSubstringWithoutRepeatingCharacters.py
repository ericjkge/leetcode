# Last updated: 2/26/2026, 9:24:17 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = right = 0
4        seen = set()
5        ans = 0
6
7        while right < len(s):
8            while left < right and s[right] in seen:
9                seen.remove(s[left])
10                left += 1
11            seen.add(s[right])
12            ans = max(ans, right - left + 1)
13            right +=1
14        
15        return ans
16