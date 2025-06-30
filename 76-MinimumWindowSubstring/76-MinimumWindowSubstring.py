# Last updated: 6/29/2025, 10:35:29 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        s_count = Counter()
        t_count = Counter(t)
        min_length = float("inf")
        ans = ""

        left = 0
        for right in range(len(s)):
            s_count[s[right]] += 1
            while all(t_count[c] <= s_count[c] for c in t_count):
                if right - left + 1 < min_length:
                    ans = s[left:right + 1]
                    min_length = right - left + 1
                s_count[s[left]] -= 1
                left += 1

        return ans

        
