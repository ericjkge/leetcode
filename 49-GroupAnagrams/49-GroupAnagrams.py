# Last updated: 3/3/2026, 8:55:41 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        anagrams = defaultdict(list)
4
5        for s in strs:
6            anagrams["".join(sorted(s))].append(s)
7        
8        return [v for v in anagrams.values()]