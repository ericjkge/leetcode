# Last updated: 5/30/2025, 12:08:00 PM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        n = len(beginWord)
        patterns = defaultdict(list)
        
        for word in wordList:
            for i in range(n):
                patterns[word[:i] + "*" + word[i+1:]].append(word) # patterns as keys, words as values
        
        def neighbors(word):
            all_options = []
            for i in range(n):
                all_options.append(word[:i] + "*" + word[i+1:])
            return all_options
                
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        
        print(neighbors(beginWord))
        
        while queue:
            word, moves = queue.popleft()
            if word == endWord:
                return moves
            for neighbor in neighbors(word):
                for pattern in patterns[neighbor]:
                    if pattern not in seen:
                        seen.add(pattern)
                        queue.append((pattern, moves + 1))
        return 0
            