# Last updated: 5/30/2025, 12:07:25 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        return len(seen) == 26
                