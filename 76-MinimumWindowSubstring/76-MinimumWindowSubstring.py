# Last updated: 7/3/2025, 5:34:28 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_counter = Counter(t)
        s_counter = Counter()
        left = 0
        min_length = float("inf")
        ans = ""

        for right in range(len(s)):
            s_counter[s[right]] += 1
            while all(t_counter[c] <= s_counter[c] for c in t_counter):
                if right - left + 1 < min_length:
                    ans = s[left:right + 1]
                    min_length = right - left + 1
                s_counter[s[left]] -= 1
                left += 1
                
        return ans
