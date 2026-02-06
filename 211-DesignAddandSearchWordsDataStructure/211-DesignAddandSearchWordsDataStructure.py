# Last updated: 2/6/2026, 10:33:59 AM
1class TrieNode():
2    def __init__(self):
3        self.children = {}
4        self.is_end = False
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
24                for c, n in node.children.items():
25                    if self.dfs(word[i + 1:], n):
26                        return True
27                return False
28            else:
29                if c not in node.children:
30                    return False
31            node = node.children[c]
32        return node.is_end
33
34    def search(self, word: str) -> bool:
35        return self.dfs(word, self.root)
36
37
38# Your WordDictionary object will be instantiated and called as such:
39# obj = WordDictionary()
40# obj.addWord(word)
41# param_2 = obj.search(word)