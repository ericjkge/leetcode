# Last updated: 11/5/2026, 10:50:04 PM
1class Solution:
2    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
3        n, m = len(spells), len(potions)
4        pairs = [0] * n
5        potions.sort()
6
7        def test(x, y):
8            return x * y >= success
9
10        for i, spell in enumerate(spells):
11            left, right = 0, m - 1
12            while left + 1 < right:
13                mid = (left + right) // 2
14                if test(spell, potions[mid]):
15                    right = mid
16                else:
17                    left = mid
18            if test(spell, potions[left]):
19                pairs[i] = m - left
20            elif test(spell, potions[right]):
21                pairs[i] = m - right
22        
23        return pairs