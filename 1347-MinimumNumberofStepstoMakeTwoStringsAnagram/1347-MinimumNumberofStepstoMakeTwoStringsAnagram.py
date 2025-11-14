# Last updated: 11/14/2025, 11:51:39 AM
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())