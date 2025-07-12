# Last updated: 7/12/2025, 3:47:03 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter] += 1

        ans = 0
        max_odd = -float("inf")
        has_odd = False
        for freq in hashmap.values():
            if freq % 2 == 0:
                ans += freq
            else:
                has_odd = True
                ans += freq - 1
                
        ans += 1 if has_odd else 0
        return ans