# Last updated: 8/6/2025, 7:38:09 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        seen = set()
        left, right = 0, 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1

        return ans