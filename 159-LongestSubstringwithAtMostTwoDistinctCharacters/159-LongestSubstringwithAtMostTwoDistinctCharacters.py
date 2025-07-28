# Last updated: 7/28/2025, 6:12:47 PM
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashmap = {}
        left = right = 0
        ans = 0
        
        while right < len(s):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            while len(hashmap) > 2:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans