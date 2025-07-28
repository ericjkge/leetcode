# Last updated: 7/28/2025, 10:14:53 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        min_length = float("inf")
        left = right = 0
        t_counter = {}
        s_counter = {}
        
        for c in t:
            t_counter[c] = t_counter.get(c, 0) + 1
        
        while right < len(s):
            s_counter[s[right]] = s_counter.get(s[right], 0) + 1
            while all(t_counter[c] <= s_counter.get(c, 0) for c in t_counter):
                if right - left + 1 < min_length:
                    ans = s[left:right + 1]
                    min_length = right - left + 1
                s_counter[s[left]] -= 1
                if s_counter[s[left]] == 0:
                    del s_counter[s[left]]
                left += 1
            right += 1
        
        return ans

        
