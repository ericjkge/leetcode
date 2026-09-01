# Last updated: 9/1/2026, 9:45:27 AM
1class Solution:
2    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
3        longest = ""
4        dictionary.sort()
5
6        for word in dictionary:
7            p1 = p2 = 0
8            while p1 < len(s) and p2 < len(word):
9                if s[p1] == word[p2]:
10                    p1 += 1
11                    p2 += 1
12                else:
13                    p1 += 1
14            
15            if p2 == len(word):
16                if len(word) > len(longest):
17                    longest = word
18        
19        return longest