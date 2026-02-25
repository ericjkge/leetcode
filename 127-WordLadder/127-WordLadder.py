# Last updated: 2/25/2026, 4:29:26 PM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        if endWord not in wordList:
4            return 0
5        
6        patterns = defaultdict(list)
7        for word in wordList:
8            for i in range(len(word)):
9                patterns[word[:i] + "*" + word[i + 1:]].append(word)
10        
11        def neighbors(word):
12            neighbors = []
13            for i in range(len(word)):
14                neighbors.append(word[:i] + "*" + word[i + 1:])
15            return neighbors
16        
17        queue = deque([beginWord])
18        seen = set()
19        counter = 1
20        
21        while queue:
22            for _ in range(len(queue)):
23                word = queue.popleft()
24
25                if word == endWord:
26                    return counter
27
28                for neighbor in neighbors(word):
29                    for option in patterns[neighbor]:
30                        if option not in seen:
31                            seen.add(option)
32                            queue.append(option)
33            
34            counter += 1
35
36        return 0
37        