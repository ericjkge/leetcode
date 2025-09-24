# Last updated: 9/24/2025, 10:43:20 AM
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashmap = {}
        left = right = ans = 0

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