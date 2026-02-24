# Last updated: 2/24/2026, 10:02:42 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        left = right = 0
4        s_counter = Counter()
5        t_counter = Counter(t)
6        ans = None
7
8        while right < len(s):
9            s_counter[s[right]] += 1
10            while all(s_counter[k] >= t_counter[k] for k in t_counter.keys()):
11                if not ans or right - left + 1 < len(ans):
12                    ans = s[left:right + 1]
13                s_counter[s[left]] -= 1
14                left += 1
15            right += 1 
16
17        return ans if ans else ""