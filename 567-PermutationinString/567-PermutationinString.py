# Last updated: 7/4/2025, 4:08:36 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            if Counter(s2[i:i+len(s1)]) == s1_count:
                return True
        
        return False