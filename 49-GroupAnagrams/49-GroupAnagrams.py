# Last updated: 6/14/2026, 10:37:11 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        anagrams = defaultdict(list)
4
5        for s in strs:
6            chars = sorted(list(s))
7            letters = "".join(chars)
8            anagrams[letters].append(s)
9        
10        return [l for l in anagrams.values()]