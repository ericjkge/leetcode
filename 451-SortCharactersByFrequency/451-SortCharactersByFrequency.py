# Last updated: 7/4/2025, 11:18:37 AM
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        chars = []
        for char, freq in counter.most_common():
            chars.append(char * freq)
        
        return "".join(chars)