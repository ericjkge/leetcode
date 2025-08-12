# Last updated: 8/12/2025, 1:28:46 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        window = set()

        while right < len(s):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            longest = max(longest, len(window))
            right += 1

        return longest