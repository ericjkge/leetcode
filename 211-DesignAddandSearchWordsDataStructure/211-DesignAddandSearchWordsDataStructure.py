# Last updated: 8/3/2025, 11:37:39 PM
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
    
    def dfs(self, node, string):
        for i in range(len(string)):
            if string[i] == ".":
                for child in node.children.values():
                    if self.dfs(child, string[i + 1:]):
                        return True
            if string[i] not in node.children:
                return False
            node = node.children[string[i]]
        return node.is_end
        
    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node, word)
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)