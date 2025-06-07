# Last updated: 6/7/2025, 12:21:17 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter] += 1
        
        max_odd = 0
        ans = 0
        for letter in hashmap:
            if hashmap[letter] % 2 == 1:
                if hashmap[letter] <= max_odd:
                    ans += hashmap[letter] - 1
                else:
                    if max_odd != 0:
                        ans += max_odd - 1
                    max_odd = hashmap[letter]
            else:
                ans += hashmap[letter]
        
        print(ans)
        print(max_odd)
        return ans + max_odd
        
        