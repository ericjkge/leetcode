# Last updated: 7/20/2026, 9:57:02 PM
1class Solution:
2    def closeStrings(self, word1: str, word2: str) -> bool:
3        if len(word1) != len(word2):
4            return False
5            
6        c1, c2 = Counter(word1), Counter(word2)
7        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())