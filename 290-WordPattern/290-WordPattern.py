# Last updated: 7/4/2025, 9:20:14 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen1 = {}
        seen2 = {}

        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in seen1 and seen1[pattern[i]] != s[i]:
                return False
            if s[i] in seen2 and seen2[s[i]] != pattern[i]:
                return False
            seen1[pattern[i]] = s[i]
            seen2[s[i]] = pattern[i]
        
        return True