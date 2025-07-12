# Last updated: 7/12/2025, 3:58:33 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # remove if unnecessary
        s.sort()
        g_index = s_index = 0
        while s_index < len(s) and g_index < len(g):
            if s[s_index] >= g[g_index]:
                s_index += 1
                g_index += 1
            else:
                s_index += 1

        return g_index