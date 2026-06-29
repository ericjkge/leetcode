# Last updated: 6/28/2026, 11:04:04 PM
1class Solution:
2    def numOfStrings(self, patterns: List[str], word: str) -> int:
3        count = 0
4        
5        for pattern in patterns:
6            if pattern in word:
7                count += 1
8        
9        return count