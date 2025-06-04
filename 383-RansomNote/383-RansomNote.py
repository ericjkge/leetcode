# Last updated: 6/4/2025, 10:13:38 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequencies = defaultdict(int)
        for char in magazine:
            frequencies[char] = frequencies.get(char, 0) + 1
        

        for c in ransomNote:
            if frequencies[c] > 0:
                frequencies[c] -= 1
            else:
                return False
        
        return True