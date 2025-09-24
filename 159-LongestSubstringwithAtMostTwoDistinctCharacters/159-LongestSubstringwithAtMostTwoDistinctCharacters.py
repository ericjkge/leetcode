# Last updated: 9/24/2025, 10:42:24 AM
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
            # print(hashmap, hashmap.values(), sum(hashmap.values()))
            ans = max(ans, sum(hashmap.values()))
            right += 1

        return ans