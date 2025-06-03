# Last updated: 6/3/2025, 3:13:52 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = ans = 0
        chars = {}
        while right < len(s):
            r = s[right]
            chars[r] = chars.get(r, 0) + 1
            while chars[r] > 1:
                l = s[left]
                chars[l] = chars.get(l, 0) - 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
        
        