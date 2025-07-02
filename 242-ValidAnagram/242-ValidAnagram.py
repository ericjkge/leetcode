# Last updated: 7/2/2025, 1:56:56 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)