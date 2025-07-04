# Last updated: 7/4/2025, 10:04:27 AM
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap = defaultdict()
        for src, des in paths:
            hashmap[src] = des
        
        start = paths[0][0]
        while start in hashmap:
            start = hashmap[start]
        
        return start
