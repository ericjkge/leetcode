# Last updated: 7/2/2025, 6:29:17 PM
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

        while queue:
            word, moves = queue.popleft()
            if word == endWord:
                return moves
            for neighbor in neighbors(word):
                for word in patterns[neighbor]:
                    if word not in seen:
                        seen.add(word)
                        queue.append((word, moves + 1))
        
        return 0

