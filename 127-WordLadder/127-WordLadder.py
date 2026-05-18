# Last updated: 5/18/2026, 4:01:12 PM
1class Solution:
2    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
3        patterns = defaultdict(list) # [hit:[*it, h*t, hi*], dot:[*ot, d*t, do*], ...]
4
5        for word in wordList:
6            for i in range(len(word)):
7                patterns[word[:i] + "*" + word[i + 1:]].append(word)
8    
9        def neighbors(word):
10            lst = []
11            for i in range(len(word)):
12                neighbor = word[:i] + "*" + word[i + 1:]
13                if neighbor in patterns:
14                    lst.extend(patterns[neighbor])
15            return set(lst)
16        
17        queue = deque([beginWord])
18        seen = set()
19        counter = 0
20        while queue:
21            for _ in range(len(queue)):
22                word = queue.popleft()
23                if word == endWord:
24                    return counter + 1
25                for neighbor in neighbors(word):
26                    if neighbor not in seen:
27                        seen.add(neighbor)
28                        queue.append(neighbor)
29            counter += 1
30        return 0