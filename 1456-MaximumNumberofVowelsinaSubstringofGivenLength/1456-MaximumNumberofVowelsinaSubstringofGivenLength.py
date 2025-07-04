# Last updated: 7/3/2025, 11:04:32 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        left = counter = 0

        for right in range(len(s)):
            if s[right] in vowels:
                counter += 1
            while right - left + 1 > k:
                if s[left] in vowels:
                    counter -= 1
                left += 1
            max_vowels = max(max_vowels, counter)

        return max_vowels



