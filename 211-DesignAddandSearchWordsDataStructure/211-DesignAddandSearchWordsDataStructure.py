# Last updated: 10/16/2025, 10:38:20 AM
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

    def dfs(self, s_index, s_node, word):
        node = s_node
        for i in range(s_index, len(word)):
            if word[i] == ".":
                for child_node in node.children.values():
                    if self.dfs(i + 1, child_node, word):
                        return True
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
        return node.is_end

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)