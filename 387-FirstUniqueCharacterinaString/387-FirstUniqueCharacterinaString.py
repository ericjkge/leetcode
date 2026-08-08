# Last updated: 8/8/2026, 4:16:45 PM
1class Solution:
2    def firstUniqChar(self, s: str) -> int:
3        freqs = Counter(s)
4
5        for i, ch in enumerate(s):
6            if freqs[ch] == 1:
7                return i
8        
9        return -1