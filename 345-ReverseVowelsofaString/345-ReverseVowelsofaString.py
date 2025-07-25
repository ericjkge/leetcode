# Last updated: 7/25/2025, 11:46:52 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        p1, p2 = 0, len(s) - 1
        chars = [char for char in s]
        vowels = "aeiouAEIOU"
        
        while p1 < p2:
            if chars[p1] in vowels and chars[p2] in vowels:
                chars[p1], chars[p2] = chars[p2], chars[p1]
                p1 += 1
                p2 -= 1
            elif chars[p1] in vowels:
                p2 -= 1
            elif chars[p2] in vowels:
                p1 += 1
            else:
                p1 += 1
                p2 -= 1
        
        return "".join(chars)