# Last updated: 8/18/2026, 10:26:13 AM
1class Solution:
2    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
3        pairs = []
4        potions.sort()
5
6        def search(spell):
7            left, right = 0, len(potions) - 1
8            while left + 1 < right:
9                mid = (left + right) // 2
10                if spell * potions[mid] < success:
11                    left = mid
12                else:
13                    right = mid
14            
15            if spell * potions[left] >= success:
16                return left
17            if spell * potions[right] >= success:
18                return right
19            return len(potions)
20
21        for spell in spells:
22            index = search(spell)
23            pairs.append(len(potions) - index)
24
25        return pairs