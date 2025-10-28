# Last updated: 10/28/2025, 9:45:24 AM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        tcounter = Counter(t)
        scounter = {}
        min_length = float("inf")
        ans = ""
        have = 0
        need = len(tcounter)

        while right < len(s):
            scounter[s[right]] = scounter.get(s[right], 0) + 1
            if s[right] in tcounter and scounter[s[right]] == tcounter[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    ans = s[left:right + 1]
                scounter[s[left]] = scounter[s[left]] - 1
                if s[left] in tcounter and scounter[s[left]] < tcounter[s[left]]:
                    have -= 1
                left += 1
            right += 1
        
        return ans