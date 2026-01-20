# Last updated: 1/20/2026, 10:28:02 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        anagrams = defaultdict(list)
4
5        for s in strs:
6            letters = "".join(sorted(s))
7            anagrams[letters].append(s)
8        
9        return [v for v in anagrams.values()]
10            