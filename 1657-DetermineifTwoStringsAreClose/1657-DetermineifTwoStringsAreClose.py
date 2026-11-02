# Last updated: 11/2/2026, 4:06:38 PM
1class Solution:
2    def closeStrings(self, word1: str, word2: str) -> bool:
3        freqs1, freqs2 = Counter(word1), Counter(word2)
4
5        return set(freqs1.keys()) == set(freqs2.keys()) and sorted(freqs1.values()) == sorted(freqs2.values())