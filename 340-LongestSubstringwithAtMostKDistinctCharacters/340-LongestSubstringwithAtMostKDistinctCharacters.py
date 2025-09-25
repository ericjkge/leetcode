# Last updated: 9/25/2025, 9:36:45 AM
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashmap = {}
        left = right = ans = 0

        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            while len(hashmap) > k:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans
        
