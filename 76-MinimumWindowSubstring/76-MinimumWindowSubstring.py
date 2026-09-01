# Last updated: 9/1/2026, 11:24:20 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        left = right = 0
4        ans = None
5        freqs1, freqs2 = Counter(), Counter(t)
6
7        while right < len(s):
8            freqs1[s[right]] += 1
9            while all(freqs1[c] >= freqs2[c] for c in freqs2):
10                if ans is None or right - left + 1 < len(ans):
11                    ans = s[left:right + 1]
12                freqs1[s[left]] -= 1
13                left += 1
14            
15            right += 1
16
17        return ans if ans is not None else ""