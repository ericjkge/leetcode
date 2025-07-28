# Last updated: 7/28/2025, 9:23:48 PM
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hashmap = {}
        left = right = 0
        ans = 0
        
        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            while len(hashmap) > k:
                hashmap[s[left]] -= 1
                if hashmap.get(s[left]) == 0:
                    del hashmap[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans
        