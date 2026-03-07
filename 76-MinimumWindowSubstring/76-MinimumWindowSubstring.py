# Last updated: 3/7/2026, 11:29:44 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        s_counter = defaultdict(int)
4        t_counter = Counter(t)
5        left = right = 0
6        ans = None
7
8        while right < len(s):
9            s_counter[s[right]] += 1
10            while all(s_counter[c] >= t_counter[c] for c in t_counter.keys()):
11                if ans is None or right - left + 1 < len(ans):
12                    ans = s[left:right + 1]
13                s_counter[s[left]] -= 1
14                left += 1
15            right += 1
16        
17        return ans if ans else ""