# Last updated: 12/30/2025, 11:31:12 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        return Counter(s) == Counter(t)