# Last updated: 5/8/2026, 8:42:25 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        left = right = 0
4        freqs = defaultdict(int)
5        substring = 0
6
7        while right < len(s):
8            freqs[s[right]] += 1
9            while sum(freqs.values()) - max(freqs.values()) > k:
10                freqs[s[left]] -= 1
11                left += 1
12            substring = max(substring, right - left + 1)
13            right += 1
14
15        return substring