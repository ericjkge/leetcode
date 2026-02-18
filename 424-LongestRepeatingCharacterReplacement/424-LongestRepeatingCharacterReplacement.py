# Last updated: 2/18/2026, 2:34:04 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        left = right = 0
4        window = defaultdict(int)
5        longest = 0
6
7        while right < len(s):
8            window[s[right]] += 1
9            while left < right and sum(window.values()) - max(window.values()) > k:
10                window[s[left]] -= 1
11                left += 1
12            longest = max(longest, right - left + 1)
13            right += 1
14        
15        return longest
16