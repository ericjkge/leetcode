# Last updated: 11/18/2025, 11:33:40 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)
        
        for s in strs:
            mappings["".join(sorted(s))].append(s)
        
        return [l for l in mappings.values()]