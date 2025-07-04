# Last updated: 7/4/2025, 4:31:34 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen1 = {}
        seen2 = {}
        for i in range(len(s)):
            if s[i] in seen1 and seen1[s[i]] != t[i]:
                return False
            if t[i] in seen2 and seen2[t[i]] != s[i]:
                return False
            seen1[s[i]] = t[i]
            seen2[t[i]] = s[i]
        
        return True