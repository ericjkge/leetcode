# Last updated: 11/21/2025, 2:45:30 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:k])

        if c1 == c2:
            return True

        for i in range(k, len(s2)):
            c2[s2[i]] += 1
            removed = s2[i - k]
            c2[removed] -= 1
            if c2[removed] == 0:
                del c2[removed]

            if c1 == c2:
                return True
                
        return False