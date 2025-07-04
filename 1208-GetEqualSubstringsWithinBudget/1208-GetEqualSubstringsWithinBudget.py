# Last updated: 7/3/2025, 11:28:52 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = cost = max_length = 0

        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length