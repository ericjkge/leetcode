# Last updated: 6/30/2025, 1:18:16 AM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = Counter()
        p_count = Counter(p)
        ans = []
        n = len(p)

        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if right >= n:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if window == p_count:
                ans.append(left)
        return ans