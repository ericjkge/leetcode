# Last updated: 4/8/2026, 10:44:59 AM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        return Counter(s) == Counter(t)