# Last updated: 8/3/2025, 11:45:30 PM
class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_end = True
    
    def dfs(self, node, word, start):
        for i in range(start, len(word)):
            if word[i] == ".":
                for child in node.children.values():
                    if self.dfs(child, word, i + 1):
                        return True
                return False
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.is_end
        
    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
    

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)