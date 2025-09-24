# Last updated: 9/24/2025, 10:26:11 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = right = ans = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, len(seen))
            right += 1

        return ans