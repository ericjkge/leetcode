# Last updated: 7/12/2025, 3:56:56 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # remove if unnecessary
        s.sort()
        g_index = s_index = ans = 0
        while s_index < len(s) and g_index < len(g):
            if s[s_index] >= g[g_index]:
                ans += 1
                s_index += 1
                g_index += 1
            else:
                s_index += 1

        return ans