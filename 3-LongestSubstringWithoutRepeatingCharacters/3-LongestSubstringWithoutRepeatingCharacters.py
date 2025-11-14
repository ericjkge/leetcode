# Last updated: 11/13/2025, 11:12:24 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = 0
        ans = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            seen.add(s[right])
            right += 1

        return ans