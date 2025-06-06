# Last updated: 6/6/2025, 9:11:51 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = ans = 0
        seen = set()
        while right < len(s):
            r = s[right]
            if r not in seen:
                seen.add(r)
                ans = max(ans, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return ans
        
        