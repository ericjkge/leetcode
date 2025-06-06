# Last updated: 6/6/2025, 9:07:56 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        n = len(s)
        seen = {s[0]:1}
        print(seen)
        left = right = 0
        ans = 1

        while right < n - 1:
            right += 1
            seen[s[right]] = seen.get(s[right], 0) + 1
            while seen[s[right]] > 1:
                seen[s[left]] = seen.get(s[left], 0) - 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans