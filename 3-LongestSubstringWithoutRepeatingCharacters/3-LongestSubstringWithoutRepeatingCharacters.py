# Last updated: 11/6/2025, 12:36:44 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = right = 0

        while right < len(s):
            while left < right and s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest