# Last updated: 5/30/2025, 12:08:06 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        ans = 0
        tracker = {}
        
        for right in range(len(s)):
            tracker[s[right]] = tracker.get(s[right], 0) + 1
            
            while tracker[s[right]] > 1:
                tracker[s[left]] = tracker.get(s[left], 0) - 1
                left += 1
                
            ans = max(ans, right - left + 1)
        return ans
        
        
        