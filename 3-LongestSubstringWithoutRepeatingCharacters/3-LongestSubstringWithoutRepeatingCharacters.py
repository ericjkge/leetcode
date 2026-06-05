# Last updated: 6/5/2026, 4:59:55 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        longest = 0
5        left = right = 0
6
7        while right < len(s):
8            while s[right] in seen:
9                seen.remove(s[left])
10                left += 1
11            
12            seen.add(s[right])
13            longest = max(longest, right - left + 1)
14            right +=1 
15        
16        return longest