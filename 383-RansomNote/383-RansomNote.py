# Last updated: 5/30/2025, 12:07:53 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        
        dic = {}
        
        for char in magazine:
            dic[char] = dic.get(char, 0) + 1

        for char in ransomNote:
            if dic.get(char, 0) <= 0:
                return False
            else:
                dic[char] -= 1
        
        return True