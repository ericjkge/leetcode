# Last updated: 11/21/2025, 2:39:10 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        c1 = Counter(s1)
        left = 0
        right = len(s1) - 1
        c2 = defaultdict(int)

        for i in range(len(s1)):
            c2[s2[i]] += 1

        if c1 == c2:
            return True

        while right < len(s2) - 1:
            right += 1
            c2[s2[right]] += 1
            c2[s2[left]] -= 1
            if c2[s2[left]] == 0:
                del c2[s2[left]]
            left += 1
            if c1 == c2:
                return True

        return False