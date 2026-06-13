# Last updated: 6/12/2026, 6:31:48 PM
1class Solution:
2    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
3        def findWeight(word):
4            total = 0
5            for letter in word:
6                total += weights[(ord(letter) - ord("a"))]
7            return total
8
9        res = []
10        for word in words:
11            index = findWeight(word) % 26
12            res.append(chr(97+(25-index)))
13
14        return "".join(res)