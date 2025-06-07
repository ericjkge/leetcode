# Last updated: 6/7/2025, 12:23:13 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = defaultdict(int)

        for letter in s:
            hashmap[letter] += 1
        
        has_odd = False
        ans = 0
        for letter in hashmap:
            if hashmap[letter] % 2 == 0:
                ans += hashmap[letter]
            else:
                has_odd = True
                ans += hashmap[letter] - 1

        return ans + 1 if has_odd else ans