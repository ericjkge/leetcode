# Last updated: 9/1/2026, 10:27:56 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        left = right = 0
4        longest = 0
5        seen = set()
6
7        while right < len(s):
8            while s[right] in seen:
9                seen.remove(s[left])
10                left += 1
11            
12            longest = max(longest, right - left + 1)
13            seen.add(s[right])
14            right += 1
15        
16        return longest