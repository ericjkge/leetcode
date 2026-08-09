# Last updated: 8/9/2026, 2:46:08 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        ans = None
4        left = right = 0
5        s_freqs = Counter()
6        t_freqs = Counter(t)
7
8        while right < len(s):
9            s_freqs[s[right]] += 1
10            while all(s_freqs[c] >= t_freqs[c] for c in t_freqs):
11                if ans is None or right - left + 1 < len(ans):
12                    ans = s[left:right + 1]
13                s_freqs[s[left]] -= 1
14                left += 1
15            right += 1
16        
17        return ans if ans is not None else ""