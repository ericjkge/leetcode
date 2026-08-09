# Last updated: 8/9/2026, 2:45:27 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        length = float("inf")
4        ans = ""
5        left = right = 0
6        s_freqs = Counter()
7        t_freqs = Counter(t)
8
9        while right < len(s):
10            s_freqs[s[right]] += 1
11            while all(s_freqs[c] >= t_freqs[c] for c in t_freqs):
12                if right - left + 1 < length:
13                    length = min(length, right - left + 1)
14                    ans = s[left:right + 1]
15                s_freqs[s[left]] -= 1
16                left += 1
17            right += 1
18        
19        return ans