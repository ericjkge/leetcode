# Last updated: 10/28/2025, 9:39:58 AM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        tcounter = Counter(t)
        scounter = {}
        min_length = float("inf")
        ans = ""

        while right < len(s):
            scounter[s[right]] = scounter.get(s[right], 0) + 1
            while all(scounter.get(c, 0) >= tcounter[c] for c in tcounter):
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    ans = s[left:right + 1]
                scounter[s[left]] = scounter[s[left]] - 1
                left += 1
            right += 1
        
        return ans