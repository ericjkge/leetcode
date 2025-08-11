# Last updated: 8/11/2025, 11:39:08 PM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        n = len(beginWord)
        patterns = defaultdict(list)
        
        for word in wordList:
            for i in range(n):
                patterns[word[:i] + "*" + word[i + 1:]].append(word)
        
        def neighbors(word):
            options = []
            for i in range(n):
                options.append(word[:i] + "*" + word[i + 1:])
            return options
        
        queue = deque([beginWord])
        seen = set([beginWord])
        moves = 1
        
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return moves
                for neighbor in neighbors(word):
                    for w in patterns[neighbor]:
                        if w not in seen:
                            seen.add(w)
                            queue.append(w)
            moves += 1
        
        return 0
