# Last updated: 4/3/2026, 9:54:04 AM
1class TrieNode:
2    def __init__(self):
3        self.is_end = False
4        self.children = {}
5
6class WordDictionary:
7
8    def __init__(self):
9        self.root = TrieNode()
10
11    def addWord(self, word: str) -> None:
12        node = self.root
13        for c in word:
14            if c not in node.children:
15                node.children[c] = TrieNode()
16            node = node.children[c]
17        node.is_end = True
18
19    def dfs(self, word, start):
20        node = start
21        for i in range(len(word)):
22            c = word[i]
23            if c == ".":
24                for child in node.children.values():
25                    if self.dfs(word[i + 1:], child):
26                        return True
27                return False
28            if c not in node.children:
29                return False
30            node = node.children[c]
31        return node.is_end
32
33    def search(self, word: str) -> bool:
34        return self.dfs(word, self.root)
35
36
37# Your WordDictionary object will be instantiated and called as such:
38# obj = WordDictionary()
39# obj.addWord(word)
40# param_2 = obj.search(word)