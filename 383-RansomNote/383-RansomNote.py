# Last updated: 6/4/2025, 10:16:03 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequencies = Counter(magazine)
        

        for c in ransomNote:
            if frequencies[c] > 0:
                frequencies[c] -= 1
            else:
                return False
        
        return True