# Last updated: 7/28/2025, 5:57:40 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        ans = 0
        seen = set()
        
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, len(seen))
            right += 1
            
        return ans
        