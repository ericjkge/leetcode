# Last updated: 6/4/2025, 10:17:19 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False

        frequencies = Counter(magazine)
        
        for c in ransomNote:
            if frequencies[c] > 0:
                frequencies[c] -= 1
            else:
                return False
        
        return True